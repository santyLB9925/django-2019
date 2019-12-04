from django.db import models
from django.utils import timezone
from Carrera.models import Carrera
class Alumno(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidos = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=254, null=False)
    direccion = models.CharField(max_length=254, null=False)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Alumno'  



