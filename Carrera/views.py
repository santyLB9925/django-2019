from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Carrera.models import Carrera
from Carrera.serializer import CarreraSerializers

# Create your views here.
class CarreraLista(APIView):
    def post(self, request, format=None):
        serializer = CarreraSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas["id"])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        queryset = Carrera.objects.filter(delete=False)
        serializer = CarreraSerializers(queryset, many=True)
        return Response(serializer.data)

class CarreraDetalle(APIView):
    def put(self, request, id, format=None):
        carrera = self.get_object(id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(carrera, status = status.HTTP_400_BAD_REQUEST)            

    def get_object(self, id):
        try:
            return Carrera.objects.get(pk=id)
        except Carrera.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        carrera = self.get_object(id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera)
            return Response(serializer.data)
        else:
            return Response(carrera)

    def delete(self, request, id,format=None):

        Carrera = self.get_object(id)
        Carrera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
