#importacoes
from rest_framework import serializers
#---------------------
from produto.modelos.produto import Produto
#serializadoresS
from produto.serializadores.categoria_serial import CategoriaSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    #instancias
    categoria = CategoriaSerializer(required=True, many=True)
    
    #classes
    class Meta:
        model = Produto
        Fields = ['titulo', 'descricao', 'preco', 'ativo', 'categoria']