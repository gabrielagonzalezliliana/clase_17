
from django.urls import path
from Clases_Coder.views import saludo, dia_hoy, muestra_nombre, probando_template
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name ='Inicio'), 
    path("cursos/", views.cursos, name = 'cursos'),
    path("estudiantes/", views.estudiantes, name='Estudiantes'),
    path('profesores/', views.profesores),
    path("entregables/", views.entregables),
    path('curso_formulario/', views.curso_formulario, name="curso_formulario"),
    path('form_con_api/', views.form_con_api, name="form_con_api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="buscar_form_con_api"),
    path('update-course/<curso_id>/', views.update_course, name ='update_course'),
    path('delete/<int:curso_id>/', views.delete, name='delete'),

    path('cursos-lista/', views.CursoListView.as_view(), name = "ListaCursos"),
    path('cursos-ver/<pk>/', views.CursoDetailView.as_view(), name= "DetalleCurso"),
    path('cursos-nuevo/', views.CursoCreateView.as_view(), name = "NuevoCurso"),
    path('cursos-editar/<pk>/', views.CursoUpdateView.as_view(), name = "EditarCurso"),  
    path('cursos-borrar/<pk>/', views.CursoDeleteView.as_view(), name = "BorrarCurso")      
]

