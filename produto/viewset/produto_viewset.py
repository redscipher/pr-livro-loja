#importacoes
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#---------------------------------
from produto.modelos import Produto
from produto.serializadores import ProdutoSerializer

class ProdutoViewset(ModelViewSet):
    #
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Produto.objects.all().order_by('id')
    
    def get_serializer_class(self):
        return ProdutoSerializer