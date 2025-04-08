# == importacoes
# django
from django.urls import path, include

# rest
from rest_framework import routers

# --------------------
from produto.viewset import ProdutoViewset, CategoriaViewset

# cria um controlador de rotas
rotasControle = routers.SimpleRouter()
# registra as views
rotasControle.register(r"produto", ProdutoViewset, basename="produto")
rotasControle.register(r"categoria", CategoriaViewset, basename="categoria")

# rotas
urlpatterns = [path("", include(rotasControle.urls))]
