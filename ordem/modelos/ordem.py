#importacoes
from django.db import models
#django
from django.contrib.auth.models import User
#-----------------------
from produto.modelos import Produto

class Ordem(models.Model):
    #atributos
    produto = models.ManyToManyField(Produto, blank=False)
    #usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)