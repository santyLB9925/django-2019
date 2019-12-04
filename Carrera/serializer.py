# -------------AGREGANDO LIBRERIAS FRAMEWORK-----------
from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from Carrera.models import Carrera


class CarreraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('__all__')