#importacoes
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#---------------------------------
from produto.modelos import Categoria
from produto.serializadores import CategoriaSerializer

class CategoriaViewset(ModelViewSet):
    #
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #retorna uma instancia da classe serializadora
    serializer_class = CategoriaSerializer
    #conjunto
    queryset = Categoria.objects.all().order_by('id')