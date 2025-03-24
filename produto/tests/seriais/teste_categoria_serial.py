#importacoes
import pytest
import json
#----------------------------
from produto.fabricas import CategoriaFabrica
from produto.serializadores import CategoriaSerializer
from produto.modelos import Categoria

#o pytest injeta a fixture 'criaCategoria' automaticamente nesta funcao
@pytest.mark.django_db
def teste_categoria_serializacao():
    #cria instancia
    categoria = CategoriaFabrica()
    #aqui 'criaCategoria' ja contem a instancia criada pela fixture
    dados_serial = CategoriaSerializer.serializa(categoria)
    #converte o JSON p/ uma estrutura Python
    data_json = json.loads(dados_serial)
    #verifica que o resultado eh uma lista
    assert isinstance(data_json, list)
    #validacao
    if len(data_json) > 0:
        #verifica se o item da lista eh um dicionário
        item = data_json[0]
        assert isinstance(item, dict)
        #verifica se o dicionario possui a chave 'titulo' e o valor esperado
        assert "titulo" in item
        assert item["titulo"] == categoria.titulo
    
@pytest.mark.django_db
def teste_categoria_desserializacao():
    #instancia original
    categoria_original = CategoriaFabrica()
    #retorna objetos serializado
    dados_serial = CategoriaSerializer.serializa(categoria_original)
    #converte o gerador p/ uma lista
    dados_desserial = CategoriaSerializer.desserializa(dados_serial)
    #validacao
    if len(dados_desserial) > 0:
        categoria_desserializada = dados_desserial[0]       #posicao 0
        #verifica se o objeto retornado eh uma instancia de 'Categoria'
        assert isinstance(categoria_desserializada, Categoria)
        #verifica se os atributos correspondem aos esperados
        assert categoria_desserializada.titulo == categoria_original.titulo