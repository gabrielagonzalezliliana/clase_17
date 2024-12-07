
from django.urls import path
from Clases_Coder.views import saludo, dia_hoy, muestra_nombre, probando_template
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name ='Inicio'), 
    path("cursos/", views.cursos),
    path("estudiantes/", views.estudiantes, name='Estudiantes'),
    path('profesores/', views.profesores),
    path("entregables/", views.entregables),
    path('curso_formulario/', views.curso_formulario, name="curso_formulario"),
    path('form_con_api/', views.form_con_api, name="form_con_api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]

