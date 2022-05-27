
from django.http import HttpResponse
from django.template import loader
from app_mtv.models import Familiar

#1(nombre="Juan Ignacio", apellido="Marchueta", fecha_nacimiento='2018-10-04', edad=3)
#2(nombre="Julia", apellido="Marchueta", fecha_nacimiento='2016-02-26', edad=6)
#3(nombre="Matias", apellido="Marchueta", fecha_nacimiento='1982-05-18', edad=40)


familiar_1 = Familiar(
        nombre="Matias", 
        apellido="Marchu", 
        fecha_nacimiento='1982-05-18', 
        edad=40
        )

familiar_2 = Familiar(
        nombre="Juan", 
        apellido="Marchu", 
        fecha_nacimiento='2018-10-04', 
        edad=3
        )

familiar_3 = Familiar(
        nombre="Juli", 
        apellido="Marchu", 
        fecha_nacimiento='2016-02-26', 
        edad=6
        )

def vista_familiar1(self):

    familiar = familiar_1
    familiar.save()

    doctexto=f"Nombre: {familiar.nombre}  Apellido: {familiar.apellido}  Fecha de nacimiento: {familiar.fecha_nacimiento}  Edad:{familiar.edad}"
    
    plantilla= loader.get_template('Plantillas.template_mtv.html')
    
    doctexto = plantilla.render(doctexto)
     
    return HttpResponse(doctexto)



def vista_familiar2(self):

    familiar = familiar_2
    familiar.save()

    doctexto=f"Nombre: {familiar.nombre}  Apellido: {familiar.apellido}  Fecha de nacimiento: {familiar.fecha_nacimiento}  Edad:{familiar.edad}"
    
    plantilla= loader.get_template('Plantillas.template_mtv.html')
    
    doctexto = plantilla.render(doctexto)
    
    return HttpResponse(doctexto)



def vista_familiar3(self):

    familiar = familiar_3
    familiar.save()

    doctexto=f"Nombre: {familiar.nombre}  Apellido: {familiar.apellido}  Fecha de nacimiento: {familiar.fecha_nacimiento}  Edad:{familiar.edad}"
    
    plantilla= loader.get_template('Plantillas.template_mtv.html')
    
    doctexto = plantilla.render(doctexto)
    
    return HttpResponse(doctexto)