#importacoes
from rest_framework import serializers
#tabelas
from produto.modelos import Produto
#serializadores
from produto.serializadores.produto_serial import ProdutoSerializer

class OrdemSerializer(serializers.ModelSerializer):
    #instancia
    produto = ProdutoSerializer(required=True, many=True)
    #-------------------
    total = serializers.SerializerMethodField()
    
    def get_total(self, instancia) -> float:
        total = sum([produto.preco for produto in instancia.produto.all()])
        #retorno
        return total
    
    #classes
    class Meta:
        model = Produto
        fields = ['produto', 'total']