# importacoes
import pytest

# -----------------------------------
from ordem.fabricas import OrdemFabrica


def criaOrdem():
    # -----------------
    ordem = OrdemFabrica()
    # salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    ordem.save()
    # def retorno
    return ordem


# decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaOrdem():
    # cria uma ordem
    ordem = criaOrdem()
    # verifica se foi criado uma ordem
    assert ordem != None
    # verifica se a ordem possui usuario
    assert ordem.usuario != None
    # produto
    assert ordem.produto != None
