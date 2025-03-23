#importacoes
import pytest
#-----------------------------------
from produto.modelos import Produto
from produto.testes.modelos import criaCategoria

#decorador p/ criar um codigo que retorna um objeto reutilizavel: fixture
@pytest.fixture
def criaProduto(criaCategoria):
    #---------------------
    produto = Produto(
        titulo='Carro Flex',
        descricao='Um carro da Honda',
        preco=10,
        ativo=True,
    )
    #salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    produto.save()
    #define o relacionamento many-to-many usando o metodo .add() ou .set()
    produto.categoria.add(criaCategoria)
    #def retorno
    return produto

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaProduto(criaProduto, criaCategoria):
    #validacoes
    assert criaProduto.titulo == 'Carro Flex'
    assert criaProduto.descricao == 'Um carro da Honda'
    assert criaProduto.preco == 10
    # Verifica se o produto esta associado a categoria: 
    assert criaCategoria.titulo == 'Carro'
    assert criaCategoria in criaProduto.categoria.all()