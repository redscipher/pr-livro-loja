#importacoes
from django.db import models

class Categoria(models.Model):
    #atributos
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(max_length=200, blank=True, null=True)
    #controle
    ativo = models.BooleanField(default=True)