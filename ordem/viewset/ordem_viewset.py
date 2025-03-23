#importacoes
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
#---------------------------------
from ordem.modelos import Ordem
from ordem.serializadores import OrdemSerializer

class OrdemViewset(ModelViewSet):
    serializer_class = OrdemSerializer
    queryset = Ordem.objects.all()