from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def probando_MTV(self):

    nom = "Julia"
    ap = "Marchueta"

    diccionario = {"nombre":nom, "apellido":ap}
   
    plantilla=loader.get_template('template_mtv.html')

    loader.get_template('template_mtv.html')
    
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

   