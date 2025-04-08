# == importacoes
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# json
import json

# categoria
from produto.modelos.categoria import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    #
    # classe sobreescrita
    class Meta:
        model = Categoria
        fields = ["titulo", "slug", "descricao", "ativo"]
        extra_kwargs = {
            "slug": {
                "validators": [],  # desabilita a validacao unica p/ slug
                "required": False,
            }
        }

    # region funcoes: sobreescritas
    def create(self, validated_data):
        # se ja existir uma categoria com o mesmo slug, atualiza-a, caso contrario, cria uma nova
        instancia, criado = Categoria.objects.update_or_create(defaults=validated_data)
        return instancia

    # endregion

    #
    @staticmethod
    def serializa(categorias: list[Categoria] | Categoria) -> str:
        # se for passado uma instancia unica, encapsula em uma lista.
        if not isinstance(categorias, list):
            categorias = [categorias]
        # cria uma instancia do serializer passando a lista de objetos p/ serem serializados
        dados_serial = CategoriaSerializer(categorias, many=True)
        # converte p/ bytes
        json_bytes = JSONRenderer().render(dados_serial.data)
        # def retorno: bytes decodificados em 'uft-8'
        return json_bytes.decode("utf-8")

    @staticmethod
    def desserializa(dados: str) -> list[Categoria]:
        # converte string p/ json
        data_json = json.loads(dados)
        if not isinstance(data_json, list):
            data_json = [data_json]
        # instancia o serializador p/ deserializar os dados, many=True porque esperamos uma lista de itens
        dados_desserial = CategoriaSerializer(data=data_json, many=True)
        # valida os dados, se houver erro, uma excecao eh lancada
        dados_desserial.is_valid(raise_exception=True)
        # def retorno
        return dados_desserial.save()
