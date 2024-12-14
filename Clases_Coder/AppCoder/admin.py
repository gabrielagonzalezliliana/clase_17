from django.contrib import admin
from AppCoder.models import Curso, Estudiante, Profesor, Entregable

# Register your models here.

@admin.register(Curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ["id", "nombre", "camada"]
    ordering =("nombre", "camada")
    search_fields = ("nombre", "camada")
    list_editable = ["nombre"]
    list_filter = ("nombre",)

    """ ver despues list_display_links, list_filter, y list_per_page"""



admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)