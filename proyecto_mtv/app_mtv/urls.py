from xml.etree.ElementInclude import include
from django.urls import path
from app_mtv import views_app


urlpatterns = [
  path('misfamiliares/', views_app, name="misfamiliares"),
]










#urlpatterns = [
   
   
    
    #path('cursos', views.cursos, name="Cursos"),
    #path('profesores', views.profesores, name="Profesores"),
    #path('estudiantes', views.estudiantes, name="Estudiantes"),
    #path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
   
   
#]
