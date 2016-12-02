from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^faceDetection/', views.faceDetection, name='faceDetection'),
    url(r'^', views.index, name='index'),
]