from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Alumnos import views
 
urlpatterns = [
    re_path(r'alumnos/$', views.AlumnosInnerJoinxD.as_view()),
    re_path(r'alumnos-registro/$', views.AlumnoLista.as_view()),
    re_path(r'alumnos/(?P<id>\d+)$', views.AlumnoDetalle.as_view()),
    re_path(r'alumnoDetail/$', views.AlumnosAPIView.as_view())
]