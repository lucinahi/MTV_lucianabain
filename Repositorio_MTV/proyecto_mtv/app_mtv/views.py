from django.http import HttpResponse
from django.shortcuts import render

from proyecto_mtv.app_mtv.models import Familiar



# Create your views here.
def familiar(self):

    familiar = Familiar(nombre="Juan Ignacio", apellido="Marchueta", fecha_nacimiento='04-10-2018', edad=3)
    familiar.save()
    doctexto=f"Nombre: {familiar.nombre}  Apellido: {familiar.apellido}  Fecha de nacimiento: {familiar.fecha_nacimiento}  Edad:{familiar.edad}"

    return HttpResponse(doctexto)
