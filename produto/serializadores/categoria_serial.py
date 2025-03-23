#importacoes
from rest_framework import serializers
#-----------------------
from produto.modelos.categoria import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    
    #classes
    class Meta:
        model = Categoria
        fields = ['titulo', 'slug', 'descricao', 'ativo']