
from django.urls import path
from Clases_Coder.views import saludo, dia_hoy, muestra_nombre, probando_template
from AppCoder import views

urlpatterns = [
    path("saludo/",saludo),
    path("dia_hoy/", dia_hoy), 
    path ("nombre/<nombre>/", muestra_nombre),
    path("probando_template/", probando_template),
    path("inicio/", views.inicio)
]
