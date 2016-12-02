from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ImageProcess, Document, NearestNeighbors
from django.views.generic.edit import FormView
from .forms import FileFieldForm

def index(request):
    return render(request, 'index.html', {'form': FileFieldForm()})

def process_files(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES.getlist('file_field'))
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            #for f in files:
                #processar cada imagem
            return HttpResponseRedirect('/index/')
    else:
        form = FileFieldForm()
    return render(request, 'index.html', {'form': form})

def process_folder(request):
    originPath = request.POST.get('origin_path', False)

    config = ImageProcess()
    config.setCaffe()
    vectors, img_files = config.load_dataset(originPath)
    Process = NearestNeighbors(Xtr=vectors, img_files=img_files, images_path=originPath, labels=labels)

    # Freeing memory:
    del vectors

    my_image_url = "https://upload.wikimedia.org/wikipedia/commons/b/be/Orang_Utan%2C_Semenggok_Forest_Reserve%2C_Sarawak%2C_Borneo%2C_Malaysia.JPG"
    if not os.path.exists('image.jpg'):
        urllib.urlretrieve (my_image_url, "image.jpg")
        
    # Show it:
    image =  misc.imread('image.jpg')
    plt.imshow(image)

    Process.retrieve(config.predict_imageNet('image.jpg'))

    destinyPath = request.POST.get('destiny_path', False)

    return render(request, 'index.html', {'form': form})


def faceDetection(request):
    def processFaces(file ,object):
        # Directory with the classifier for the facesFrontais
        faceCascade = cv2.CascadeClassifier('core/haarcascade_frontalface_default.xml')
        image = cv2.imread(object)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect objects in the picture
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        # Print amount faces found
        print "Encontradas {0} faces!".format(len(faces))

        # Draw retangle in around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imwrite(file, image)
        return file

    if request.method == "GET":
       return render(request, 'faceDetection.html')
    elif request.method == "POST":
        form = request.POST
        url = form.get('Nome')

        # Get content of URL
        url_response = urllib.urlopen(url)

        # Convert into a numpy array
        image_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        imageCode = cv2.imdecode(image_array, -1)

        file = "core/static/imagens/test_image_URL.png"
        cv2.imwrite(file, imageCode)

        imageCode = file
        processFaces(file, imageCode)

    context = {'show_image': 'True'}

    return render(request, 'faceDetection.html', context)