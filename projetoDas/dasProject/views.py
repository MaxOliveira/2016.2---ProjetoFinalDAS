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
