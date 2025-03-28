#importacoes
from rest_framework.viewsets import ModelViewSet
#---------------------------------
from produto.modelos import Categoria
from produto.serializadores import CategoriaSerializer

class CategoriaViewset(ModelViewSet):
    #
    #retorna uma instancia da classe serializadora
    serializer_class = CategoriaSerializer
    #conjunto
    queryset = Categoria.objects.all().order_by('id')