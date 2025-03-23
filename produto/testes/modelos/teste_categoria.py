#importacoes
import pytest
#-----------------------------------
from produto.fabricas import CategoriaFabrica

def criaCategoria():
    #---------------------
    categoria = CategoriaFabrica()
    #salva o objeto primeiro, pois a relação many-to-many depende de uma instancia persistida
    categoria.save()
    #def retorno
    return categoria

#decorador p/ criar objetos no banco configurado
@pytest.mark.django_db
def testa_criaCategoria():
    #cria categoria
    categoria = criaCategoria()
    #validacoes
    assert categoria.titulo != ''
    assert categoria.slug != ''
    assert categoria.descricao != ''