from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})



def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppCoder/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})



from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm
 
# Vista de editar el perfil
# Obligamos a loguearse para editar los datos del usuario activo
@login_required
def editar_perfil(request):

    # El usuario para poder editar su perfil primero debe estar logueado.
    # Al estar logueado, podremos encontrar dentro del request la instancia
    # del usuario -> request.user
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)

        if miFormulario.is_valid():

            if miFormulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen = miFormulario.cleaned_data.get("imagen")
                usuario.avatar.save()

            miFormulario.save()

            # Retornamos al inicio una vez guardado los datos
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(
        request,
        "users/editar_usuario.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )


from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy("EditarPerfil")
