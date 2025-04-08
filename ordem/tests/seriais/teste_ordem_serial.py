# importacoes
import pytest
import json

# ----------------------------
from ordem.serializadores import OrdemSerializer
from ordem.fabricas import OrdemFabrica
from ordem.modelos import Ordem


# o pytest injeta a fixture 'criaCategoria' automaticamente nesta funcao
@pytest.mark.django_db
def teste_ordem_serializacao():
    # cria uma ordem
    ordem = OrdemFabrica()
    # aqui 'criaCategoria' ja contem a instancia criada pela fixture
    dados_serial = OrdemSerializer.serializa(ordem)
    # converte p/ JSON
    data_json = json.loads(dados_serial)
    # verifica se o resultado serializado eh uma lista
    assert isinstance(data_json, list)
    # validacao
    if len(data_json) > 0:
        # verifica se o item da lista eh um dicionario
        item = data_json[0]
        assert isinstance(item, dict)
        # verifica se o dicionario possui chave e o valor esperado
        assert "produto" in item
        # valida os dados do produto
        assert item["produto"] == list(ordem.produto.all())


@pytest.mark.django_db
def teste_ordem_desserializacao():
    # cria uma ordem
    ordem_original = OrdemFabrica()
    # serializa a ordem
    dados_serial = OrdemSerializer.serializa(ordem_original)
    # desserializa objeto recem serializado
    dados_desserial = OrdemSerializer.desserializa(dados_serial)
    # validacao
    if len(dados_desserial) > 0:
        # item 0
        ordem_deserializada = dados_desserial[0]
        # verifica se objeto eh uma instancia de 'ordem'
        assert isinstance(ordem_deserializada, Ordem)
        # verifica se os atributos correspondem aos da ordem original
        assert list(ordem_deserializada.produto.all()) == list(
            ordem_original.produto.all()
        )
