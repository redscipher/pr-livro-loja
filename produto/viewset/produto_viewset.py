#importacoes
from rest_framework.viewsets import ModelViewSet
#---------------------------------
from produto.modelos import Produto
from produto.serializadores import ProdutoSerializer

class ProdutoViewset(ModelViewSet):
    #
    def get_queryset(self):
        return Produto.objects.all().order_by('id')
    
    def get_serializer_class(self):
        return ProdutoSerializer