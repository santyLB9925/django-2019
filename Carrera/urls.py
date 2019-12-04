from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Carrera import views
 
urlpatterns = [
    re_path(r'carreras/$', views.CarreraLista.as_view()),
    re_path(r'ver-carreras/$', views.CarreraLista.as_view()),
    re_path(r'carrera/(?P<id>\d+)$', views.CarreraDetalle.as_view()),
    
]