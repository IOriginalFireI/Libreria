from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class libro_form(forms.ModelForm):

    class Meta:
        model = libro
        fields = ['titulo', 'descripcion', 'año',
                  'autor', 'editorial', 'imagen', 'disponible']


class userCreation(UserCreationForm):
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
