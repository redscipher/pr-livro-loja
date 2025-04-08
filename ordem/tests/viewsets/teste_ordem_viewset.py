# importacoes
import json

# rest
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

# django
from django.urls import reverse

# --------------------------------
from produto.fabricas import CategoriaFabrica, ProdutoFabrica
from ordem.fabricas import UsuarioFabrica, OrdemFabrica
from ordem.modelos import Ordem


class TesteOrdemViewset(APITestCase):
    # instancia
    cliente = APIClient()

    # region metodos
    #
    def setUp(self):
        self.usuario = UsuarioFabrica()
        # adicao do token
        token = Token.objects.create(user=self.usuario)
        token.save()
        # -----------------------------
        self.categoria = CategoriaFabrica(titulo="tecnologia")
        self.produto = ProdutoFabrica(
            titulo="mouse", preco=100, categoria=[self.categoria]
        )
        self.ordem = OrdemFabrica(produto=[self.produto])

    def test_get_Ordem(self):
        # retorna token criado
        token = Token.objects.get(user__username=self.usuario.username)
        # adiciona token na requisicao
        self.cliente.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # resposta
        response = self.cliente.get(reverse("ordem-list", kwargs={"versao": "v1"}))
        # teste
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        # efetua leitura
        ordem_data = json.loads(response.content)
        print("ordem criada:", ordem_data)
        # testes
        self.assertEqual(
            ordem_data["results"][0]["produto"][0]["titulo"], self.produto.titulo
        )
        self.assertEqual(
            ordem_data["results"][0]["produto"][0]["preco"], self.produto.preco
        )
        self.assertEqual(
            ordem_data["results"][0]["produto"][0]["ativo"], self.produto.ativo
        )
        self.assertEqual(
            ordem_data["results"][0]["produto"][0]["categoria"][0]["titulo"],
            self.categoria.titulo,
        )

    def test_post_Ordem(self):
        # usuario + produto
        produto = ProdutoFabrica()
        # pega os ids
        data = json.dumps({"produto_id": [produto.id], "usuario": self.usuario.id})
        # retorna token criado
        token = Token.objects.get(user__username=self.usuario.username)
        # adiciona token na requisicao
        self.cliente.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # resposta
        response = self.cliente.post(
            reverse("ordem-list", kwargs={"versao": "v1"}),
            data=data,
            content_type="application/json",
        )
        # teste
        print("Detalhes resposta ordem:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # usuario da ordem criada
        ordem_criada = Ordem.objects.get(usuario=self.usuario)
        # testes
        self.assertEqual(ordem_criada.usuario.id, self.usuario.id)
        self.assertEqual(ordem_criada.produto.all()[0].id, produto.id)

    #
    # endregion
