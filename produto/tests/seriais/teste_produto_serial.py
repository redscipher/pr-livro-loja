# importacoes
import pytest
import json

# ----------------------------
from produto.fabricas import ProdutoFabrica
from produto.serializadores import ProdutoSerializer
from produto.modelos import Produto


@pytest.mark.django_db
def teste_produto_serializacao():
    # cria um produto
    produto = ProdutoFabrica()
    dados_serial = ProdutoSerializer.serializa(produto)
    # converte o JSON p/ uma estrutura Python
    data_json = json.loads(dados_serial)
    # verifica que o resultado eh uma lista
    assert isinstance(data_json, list)
    # validacao
    if len(data_json) > 0:
        # verifica se o item da lista eh um dicionário
        item = data_json[0]
        assert isinstance(item, dict)
        # verifica se o dicionario possui a chave 'titulo' e o valor esperado
        assert "titulo" in item
        assert item["titulo"] == produto.titulo


@pytest.mark.django_db
def teste_produto_desserializacao():
    # cria um produto
    produto_original = ProdutoFabrica()
    # retorna objetos serializado
    dados_serial = ProdutoSerializer.serializa(produto_original)
    # desserializa
    dados_desserial = ProdutoSerializer.desserializa(dados_serial)
    # validacao
    if len(dados_desserial) > 0:
        produto_desserializado = dados_desserial[0]  # posicao 0
        # verifica se o objeto retornado eh uma instancia de 'Categoria'
        assert isinstance(produto_desserializado, Produto)
        # verifica se os atributos correspondem aos esperados
        assert produto_desserializado.titulo == produto_original.titulo
