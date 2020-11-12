from django import forms
from django.forms import ModelForm
from api.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Email','Telefono','Pnombre','Apellido','Mensaje']
