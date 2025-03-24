#== importacoes
#django
from django.urls import path, include
#rest
from rest_framework import routers
#--------------------
from ordem.viewset import OrdemViewset

#cria um controlador de rotas
rotasControle = routers.SimpleRouter()
#registra as views
rotasControle.register(r'ordem', OrdemViewset, basename='ordem')

#rotas
urlpatterns = [
    path('', include(rotasControle.urls))
]
