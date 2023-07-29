from django.db import models
from contatos.models import Contato
from django import forms

# Essa class é relacionado ao formulario dentro da dashboard do usuario
class FormContato(forms.ModelForm):
    # Esse formulario representa o model Contato
    class Meta:
        model = Contato
        # Campos que quero excluir:
        exclude = ('publicado',)
