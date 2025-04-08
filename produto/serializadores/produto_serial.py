# importacoes
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# json
import json

# ---------------------
from produto.modelos import Produto
from produto.modelos import Categoria

# serializadores
from produto.serializadores.categoria_serial import CategoriaSerializer


class ProdutoSerializer(serializers.ModelSerializer):
    #
    # classes
    class Meta:
        model = Produto
        fields = [
            "id",
            "titulo",
            "descricao",
            "preco",
            "ativo",
            "categoria",
            "categoria_id",
        ]
        extra_kwargs = {"categoria": {"required": False}}

    # instancias
    categoria = CategoriaSerializer(required=False, many=True)

    # cria novos campos na tabela
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), required=False, write_only=True, many=True
    )

    # region metodos: sobreescritos
    #
    def create(self, validated_data):
        # variavel
        campos = "categoria_id" if "categoria_id" in validated_data else "categoria"
        # extrai os dados aninhados p/ 'categoria'
        categorias_data = validated_data.pop(campos)
        # cria o produto com os dados restantes
        produto = Produto.objects.create(**validated_data)
        # cria (ou obtem) e adiciona cada categoria ao produto
        for cat_data in categorias_data:
            # aqui, chamamos o metodo create() do CategoriaSerializer
            # atencao: isso sempre cria uma nova categoria
            categoria_obj = (
                cat_data
                if campos == "categoria_id"
                else CategoriaSerializer().create(cat_data)
            )
            # adiciona a categoria
            produto.categoria.add(categoria_obj)
        # def retorno
        return produto

    #
    # endregion

    @staticmethod
    def serializa(produtos: list[Produto] | Produto) -> str:
        # se for passado uma instancia unica, encapsula em uma lista.
        if not isinstance(produtos, list):
            produtos = [produtos]
        # cria uma instancia do serializer passando a lista de objetos p/ serem serializados
        dados_serial = ProdutoSerializer(produtos, many=True)
        # converte p/ bytes
        json_bytes = JSONRenderer().render(dados_serial.data)
        # def retorno: bytes decodificados em 'uft-8'
        return json_bytes.decode("utf-8")

    @staticmethod
    def desserializa(dados: str) -> list[Produto]:
        # converte string p/ json
        data_json = json.loads(dados)
        if not isinstance(data_json, list):
            data_json = [data_json]
        # instancia o serializador p/ deserializar os dados, many=True porque esperamos uma lista de itens
        dados_desserial = ProdutoSerializer(data=data_json, many=True)
        # valida os dados, se houver erro, uma excecao eh lancada
        dados_desserial.is_valid(raise_exception=True)
        # def retorno
        return dados_desserial.save()
