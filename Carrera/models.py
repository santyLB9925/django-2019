from django.db import models
from django.utils import timezone

class Carrera(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    create = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Carrera'    


# Create your models here.