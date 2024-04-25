from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

# Autenticación de usuario.


def login_view(request):

    if request.method == "GET":
        login_form = AuthenticationForm()
        return render(request, 'login.html', {"login_form": login_form})
    else:
        login_form = AuthenticationForm(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return HttpResponse("No hay usuario")

        else:
            # Si se autentica el usuario se genera el login para su sesión.
            login(request, user)
            return redirect('libreria')

# Creación de usuarios.


def crearUsuario(request):

    if request.method == "GET":
        creation_form = userCreation()
        return render(request, 'crear_usuario.html', {"creation_form": creation_form})

    else:
        creation_form = userCreation(request.POST)
        if creation_form.is_valid():
            # Se crea el usuario con los campos agregados al modelo de User.
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                password=request.POST['password1']
            )
            try:
                user.save()
                messages.success(request, "Usuario creado")
            except Exception as e:
                messages.error(request, f"Error: {e}")
    return render(request, 'crear_usuario.html', {"creation_form": creation_form})


def libreria(request):

    form_libro = libro_form()
    libros = libro.objects.all()

    if request.method == "GET":
        return render(request, 'libreria.html', {"libros": libros, "libros_form": form_libro})
    else:
        form_libro = libro_form(request.POST, request.FILES)
        if form_libro.is_valid():
            try:
                # Se le agrega el usuario actual al libro que se agregó antes de guardarlo en la base de datos.
                nuevo_libro = form_libro.save(commit=False)
                nuevo_libro.user = request.user
                nuevo_libro.save()
                messages.success(request, "Libro guardado")
            except Exception as e:
                messages.error(f"Error: {e}")
        else:
            pass

    return render(request, 'libreria.html', {"libros": libros, "libros_form": form_libro})


# Se manda el id a la vista para buscar el objeto en la base de datos y eliminarlo.
def eliminar(request, libro_id):
    eliminar_libro = get_object_or_404(libro, pk=libro_id)
    eliminar_libro.delete()
    return redirect('libreria')


"""Se manda el id del objeto para crear un form con su instancia(datos) y poder editarlos, después de eso cuando es POST se crea de nuevo el formulario con los nuevos datos y también la
   instancia para guardar los datos que no se editaron y se queden igual a como estaban."""


def editar(request, libro_id):

    if request.method == "POST":
        editar_libro = get_object_or_404(libro, pk=libro_id)
        form_libro = libro_form(
            request.POST, request.FILES, instance=editar_libro)
        form_libro.save()
        return redirect("libreria")

    else:

        editar_libro = get_object_or_404(libro, pk=libro_id)
        form_libro = libro_form(instance=editar_libro)
        return render(request, 'editar.html', {"libro_form": form_libro})


class actualizar_informacion(UpdateView):

    model = User
    # Campos que se pueden actualizar
    fields = ['username', 'email', 'first_name', 'last_name']
    # Plantilla para la vista de actualización
    template_name = 'actualizar_informacion.html'
    # URL a la que redirigir después de una actualización exitosa
    success_url = reverse_lazy('libreria')
    
    def dispatch(self, request, *args, **kwargs):
        # Verificar si el usuario autenticado tiene permiso para editar este usuario
        if request.user.pk != self.kwargs['pk']:
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return super().dispatch(request, *args, **kwargs)

def salir(request):
    
    if request.method == "GET":
        logout(request)
        return redirect('login')
    
def cambiarContraseña(request):
    
    contraseña_form = PasswordChangeForm(request.user)
    
    if request.method == "GET":
        
        return render(request, 'cambiar_contraseña.html', {'contraseña_form': contraseña_form})
    
    else:
        
        contraseña_form = PasswordChangeForm(request.user, request.POST)
        
        if contraseña_form.is_valid():
            contraseña_form.save()
            messages.success(request, "Contraseña cambiada")
            logout(request)
            return redirect('login')
        
    return render(request, 'cambiar_contraseña.html', {'contraseña_form': contraseña_form})