from django.db import models
from django.utils import timezone

# Mexer com Base de Dados é aqui

class Categoria(models.Model):
    nome = models.CharField(max_length=60)

    # representando a essa classe pelo nome
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=60)  # campo de caracteres que recebe ate 60 charc
    sobrenome = models.CharField(max_length=60, blank=True)  # blank é pro campo ser opcional
    apelido = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=60, blank=True)
    telefone = models.CharField(max_length=60)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=True)  # Campo de marcado ou desmarcado / para mostrar ou nao o contato
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # representando a essa classe pelo nome
    def __str__(self):
        return self.nome
