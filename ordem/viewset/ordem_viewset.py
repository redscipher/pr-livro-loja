#importacoes
from rest_framework.viewsets import ModelViewSet
#---------------------------------
from ordem.modelos import Ordem
from ordem.serializadores import OrdemSerializer

class OrdemViewset(ModelViewSet):
    #retorna uma instancia da classe serializadora
    serializer_class = OrdemSerializer
    #conjunto
    queryset = Ordem.objects.all()