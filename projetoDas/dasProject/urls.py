from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^faceDetection/', views.faceDetection, name='faceDetection'),
    url(r'^load_files/', views.process_files),
    url(r'^load_folder/', views.process_folder)
]