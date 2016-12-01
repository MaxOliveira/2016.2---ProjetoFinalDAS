from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name=''),
    url(r'^load_files/', views.process_files),
    url(r'^load_folder/', views.process_folder)
]