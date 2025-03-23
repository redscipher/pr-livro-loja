#importacoes
import pytest
#-----------------------------------
from produto.fabricas import ProdutoFabrica

def criaProduto():
    #---------------------
    produto = ProdutoFabrica()
    #salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    produto.save()
    #def retorno
    return produto

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaProduto():
    #cria produto
    produto = criaProduto()
    #validacoes
    assert produto.titulo != ''
    assert produto.descricao != ''
    assert produto.preco != -1
    # Verifica se o produto esta associado a categoria: 
    assert produto.categoria.all().count() == 0