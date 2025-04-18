# importacoes
import json

# rest
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# django
from django.urls import reverse

# --------------------------------
from produto.fabricas import CategoriaFabrica
from produto.modelos import Categoria
from ordem.fabricas import UsuarioFabrica


class TesteCategoriaViewset(APITestCase):
    # instancia
    cliente = APIClient()

    # region metodos
    #
    def setUp(self):
        self.usuario = UsuarioFabrica()
        # -------------------------
        self.categoria = CategoriaFabrica(titulo="livros")

    def test_get_Categoria(self):
        # resposta
        response = self.cliente.get(reverse("categoria-list", kwargs={"versao": "v1"}))
        # teste
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # efetua leitura
        categ_data = json.loads(response.content)
        print("categoria:")
        print(categ_data)
        # testes
        self.assertEqual(categ_data["results"][0]["titulo"], self.categoria.titulo)

    def test_post_Categoria(self):
        # pega os ids
        data = json.dumps({"titulo": "tecnologia"})
        # resposta
        response = self.cliente.post(
            reverse("categoria-list", kwargs={"versao": "v1"}),
            data=data,
            content_type="application/json",
        )
        # teste
        print("Detalhes resposta categoria:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # usuario da ordem criada
        categ_criada = Categoria.objects.get(titulo="tecnologia")
        # testes
        self.assertEqual(categ_criada.titulo, "tecnologia")

    #
    # endregion
