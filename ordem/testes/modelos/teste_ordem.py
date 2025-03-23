#importacoes
import pytest
#-----------------------------------
from ordem.modelos import Ordem
from produto.testes.modelos.teste_produto import criaProduto
from ordem.fabricas import UsuarioFabrica

#decorador p/ criar um codigo que retorna um objeto reutilizavel: fixture
@pytest.fixture
def criaOrdem(criaProduto):
    #-----------------
    ordem = Ordem(usuario=UsuarioFabrica())
    #salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    ordem.save()
    #define o relacionamento many-to-many usando o metodo .add() ou .set()
    ordem.produto.add(criaProduto)
    #def retorno
    return ordem

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaOrdem(criaOrdem, criaProduto):
    # Verifica se o produto esta associado a categoria: 
    assert criaProduto.titulo == 'Carro Flex'
    assert criaProduto in criaOrdem.produto.all()