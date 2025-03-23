#importacoes
import pytest
#-----------------------------------
from produto.modelos import Categoria

#decorador p/ criar um codigo que retorna um objeto reutilizavel: fixture
@pytest.fixture
def criaCategoria():
    #---------------------
    categoria = Categoria(
        titulo='Carro',
        slug='Veiculo',
        descricao='Um veiculo de 4 rodas',
        ativo=True
    )
    #salva categoria
    categoria.save()
    #def retorno
    return categoria