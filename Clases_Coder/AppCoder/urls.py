
from django.urls import path
from Clases_Coder.views import saludo, dia_hoy, muestra_nombre, probando_template
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name ='Inicio'), 
    path("cursos/", views.cursos),
    path("estudiantes/", views.estudiantes, name='Estudiantes'),
    path("entregables/", views.entregables)
]
