#importacoes
from django.db import models
#---------------------------
from .categoria import Categoria

class Produto(models.Model):
    #atributos
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    #----------------------------
    preco = models.PositiveBigIntegerField(null=True)
    #controle
    ativo = models.BooleanField(default=True)
    #tabelas
    categoria = models.ManyToManyField(Categoria, blank=True)