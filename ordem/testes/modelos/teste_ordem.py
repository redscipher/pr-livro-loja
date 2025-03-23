#importacoes
import pytest
#-----------------------------------
from ordem.fabricas import OrdemFabrica

#decorador p/ criar um codigo que retorna um objeto reutilizavel: fixture
@pytest.fixture
def criaOrdem():
    #-----------------
    ordem = OrdemFabrica()
    #salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    ordem.save()
    #def retorno
    return ordem

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaOrdem(criaOrdem):
    # Verifica se o produto esta associado a categoria: 
    assert criaOrdem.produto.all().count() == 0