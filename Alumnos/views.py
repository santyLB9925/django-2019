from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Alumnos.models import Alumno
from Alumnos.serializer import AlumnoSerializers

class AlumnoLista(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas["id"])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class AlumnoDetalle(APIView):

    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id)
        except Alumno.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(alumno, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumno = self.get_object(id)
        Alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)             

class AlumnosAPIView(generics.ListCreateAPIView):
    search_fields = ['nombre']
    filter_backends = (filters.SearchFilter,)
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers


class AlumnosInnerJoinxD(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.select_related('carrera').all()
        alumnos = []
        for alumno in queryset:
            alumnos.append({'id': alumno.id, 'nombre': alumno.nombre, 'apellidos': alumno.apellidos, 'edad':alumno.edad,'sexo':alumno.sexo,'direccion':alumno.direccion, 'carrera': alumno.carrera.nombre})

        return Response(alumnos) 

   
    
                       
