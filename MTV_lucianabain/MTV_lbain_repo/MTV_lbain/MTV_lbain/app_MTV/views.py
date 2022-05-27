from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template


# Create your views here.
from app_MTV import familiar

def Familiar(self):
    familiar = Familiar (nombre="Julia", apellido="Marchueta", )
    familiar.save()
    respuesta = f"Nombre: {Familiar.nombre}   Apellido: {Familiar.apellido}"

    return HttpResponse(respuesta)