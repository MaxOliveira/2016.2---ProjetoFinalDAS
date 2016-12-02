from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ImageProcess, Document
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
    folderPath = request.POST.get('origin_path', False)
    folderPath = request.POST.get('destiny_path', False)

    imageProcess = ImageProcess()
    imageProcess.load_dataset(folderPath)
    return render(request, 'index.html', {'form': form})
