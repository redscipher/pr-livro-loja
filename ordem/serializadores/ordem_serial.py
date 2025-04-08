# importacoes
import json
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# tabelas
from ordem.modelos import Ordem
from produto.modelos import Produto

# serializadores
from produto.serializadores.produto_serial import ProdutoSerializer


class OrdemSerializer(serializers.ModelSerializer):
    #
    # classe configuracao: django
    class Meta:
        model = Ordem
        fields = ["usuario", "produto", "total", "produto_id"]
        extra_kwargs = {"produto": {"required": False}}

    # instancia
    produto = ProdutoSerializer(required=False, many=True)

    # propriedades
    # cria um novo campo na tabela
    total = serializers.SerializerMethodField()
    # id do produto
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), required=False, write_only=True, many=True
    )

    # region metodos: sobreescritos
    #
    def create(self, validated_data):
        # variavel
        campos = "produto_id" if "produto_id" in validated_data else "produto"
        # extrai os dados aninhados p/ 'produto'
        produtos_data = validated_data.pop(campos)
        usuario_data = validated_data.pop("usuario")
        # cria o produto com os dados restantes
        ordem = Ordem.objects.create(usuario=usuario_data)
        # cria (ou obtem) e adiciona cada produto a ordem
        for prod_data in produtos_data:
            # aqui, chamamos o metodo create() do ProdutoSerializer
            # atencao: issoS sempre cria uma nova categoria
            prod_obj = (
                prod_data
                if campos == "produto_id"
                else ProdutoSerializer().create(prod_data)
            )
            # adiciona a categoria
            ordem.produto.add(prod_obj)
        # def retorno
        return ordem

    #
    # endregion

    # region metodos
    #
    @staticmethod
    def serializa(ordens: list[Ordem] | Ordem) -> str:
        # se for passado uma instancia unica, encapsula em uma lista.
        if not isinstance(ordens, list):
            ordens = [ordens]
        # cria uma instancia do serializer passando a lista de objetos p/ serem serializados
        dados_serial = OrdemSerializer(ordens, many=True)
        # converte p/ bytes
        json_bytes = JSONRenderer().render(dados_serial.data)
        # def retorno: bytes decodificados em 'uft-8'
        return json_bytes.decode("utf-8")

    @staticmethod
    def desserializa(dados: str) -> list[Ordem]:
        # converte string p/ json
        data_json = json.loads(dados)
        if not isinstance(data_json, list):
            data_json = [data_json]
        # instancia o serializador p/ deserializar os dados, many=True porque esperamos uma lista de itens
        dados_desserial = OrdemSerializer(data=data_json, many=True)
        # valida os dados, se houver erro, uma excecao eh lancada
        dados_desserial.is_valid(raise_exception=True)
        # def retorno
        return dados_desserial.save()

    def get_total(self, instancia) -> float:
        # soma os valores dos produtos
        total = sum([produto.preco for produto in instancia.produto.all()])
        # retorno
        return total

    #
    # endregion
