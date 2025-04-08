# importacoes
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

# ---------------------------------
from ordem.modelos import Ordem
from ordem.serializadores import OrdemSerializer


class OrdemViewset(ModelViewSet):
    #
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    # retorna uma instancia da classe serializadora
    serializer_class = OrdemSerializer
    # conjunto
    queryset = Ordem.objects.all().order_by("id")
