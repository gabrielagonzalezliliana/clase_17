from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin



from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render (request, "AppCoder/show_courses.html", {"cursos": cursos})

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")



from AppCoder.models import Curso

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "AppCoder/inicio.html")

    return render(request,"AppCoder/curso_formulario.html")

from AppCoder.forms import CursoFormulario

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "AppCoder/inicio.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"mi_formulario": mi_formulario})




from AppCoder.forms import BuscaCursoForm

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/resultados.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"mi_formulario": mi_formulario})


def update_course(request, curso_id):
    try:
        curso = Curso.objects.get(id=curso_id)
    except Curso.DoesNotExist:
        return render(request, "AppCoder/inicio.html")
    
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre= data["curso"]
            curso.camada = data["camada"]
            curso.save()
            return render(request, "AppCoder/inicio.html")

    formulario = CursoFormulario(
        initial={
            "curso": curso.nombre,
            "camada": curso.camada
        }
    )
    return render(request,"AppCoder/editar_curso.html", {"form": formulario, "curso": curso})



def delete(request, curso_id):
    curso_a_borrar = Curso.objects.get(id= curso_id)
    curso_a_borrar.delete()
    return render(request, "AppCoder/inicio.html")


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CursoListView (LoginRequiredMixin,ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/curso_lista.html"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/curso_crear.html"
    success_url = reverse_lazy("ListaCursos")
    fields =["nombre", "camada"]

class CursoUpdateView(UpdateView):
    model = Curso
    template_name= "AppCoder/curso_editar.html"
    success_url = reverse_lazy ("ListaCursos")
    fields = ["nombre", "camada"]

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppCoder/curso_borrar.html"
    success_url = reverse_lazy("ListaCursos")
