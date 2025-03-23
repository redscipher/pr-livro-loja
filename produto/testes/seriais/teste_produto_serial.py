#importacoes
import pytest
from django.core import serializers
#----------------------------
from produto.fabricas import ProdutoFabrica

def retorna_serial():
    #aqui 'criaCategoria' ja contem a instancia criada pela fixture
    dados_serial = serializers.serialize('json', [ProdutoFabrica()])
    #def retorno
    return dados_serial

#o pytest injeta a fixture 'criaCategoria' automaticamente nesta funcao
@pytest.mark.django_db
def teste_produto_serializacao():
    #aqui 'criaCategoria' ja contem a instancia criada pela fixture
    dados_serial = retorna_serial()
    #testa se dados serializados possuem os atributos da categoria
    assert '"titulo"' in dados_serial
    
@pytest.mark.django_db
def teste_produto_desserializacao():
    #retorna objetos serializado
    dados_serial = retorna_serial()
    #converte o gerador p/ uma lista
    dados_desserial = list(serializers.deserialize('json', dados_serial))
    #verifica se ha exatamente um objeto desserializado
    assert len(dados_desserial) == 1
    #acessa a instancia real do modelo através do atributo .object
    produto_desserializado = dados_desserial[0].object
    #agora podemos comparar os atributos esperados
    assert produto_desserializado.titulo in dados_serial