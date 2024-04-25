"""
URL configuration for libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from biblioteca import views
from biblioteca.views import actualizar_informacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name="login" ),
    path('crearusuario/', views.crearUsuario, name="crear_usuario" ),
    path('libreria/', views.libreria, name="libreria" ),
    path('elminar/<int:libro_id>', views.eliminar, name="eliminar" ),
    path('editar/<int:libro_id>', views.editar, name="editar" ),
    path('libreria/actualizarinformacion/<int:pk>/', actualizar_informacion.as_view(), name="actualizar" ),
    path('libreria/salir/', views.salir, name="salir" ),
    path('libreria/cambiarcontraseña/', views.cambiarContraseña, name="cambiar_contraseña" )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)