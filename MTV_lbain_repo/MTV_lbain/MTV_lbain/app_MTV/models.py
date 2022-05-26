from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
   

class Datos(models.Model):
    telefono=models.IntegerField(max_length=20)
    cumpleaños=models.DateField()
    edad=models.SmallIntegerField()
