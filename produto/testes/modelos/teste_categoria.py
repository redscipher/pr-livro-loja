#importacoes
import pytest
#-----------------------------------
from conftest import criaCategoria

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaCategoria(criaCategoria):
    #validacoes
    assert criaCategoria.titulo == 'Carro'
    assert criaCategoria.slug == 'Veiculo'
    assert criaCategoria.descricao == 'Um veiculo de 4 rodas'