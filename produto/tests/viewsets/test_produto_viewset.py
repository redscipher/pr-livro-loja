#importacoes
import json
#rest
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
#django
from django.urls import reverse

#--------------------------------
from produto.fabricas import CategoriaFabrica, ProdutoFabrica
from ordem.fabricas import UsuarioFabrica
from produto.modelos import Produto

class TesteProdutoViewset(APITestCase):
    #instancia
    cliente = APIClient()
    
    #region metodos
    #
    def setUp(self):
        self.usuario = UsuarioFabrica()
        self.produto = ProdutoFabrica(titulo='controle', preco=200)
    
    def test_get_Produto(self):
        #resposta
        response = self.cliente.get(
            reverse('produto-list', kwargs={'versao': 'v1'})
        )
        #teste
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #efetua leitura
        produto_data = json.loads(response.content)
        print('produto:')
        print(produto_data)
        #testes
        self.assertEqual(produto_data[0]['titulo'], self.produto.titulo)
        self.assertEqual(produto_data[0]['preco'], self.produto.preco)
        self.assertEqual(produto_data[0]['ativo'], self.produto.ativo)
       
    def test_post_Produto(self):
        #usuario + produto
        categoria = CategoriaFabrica()
        #pega os ids
        data = json.dumps({
            'titulo': 'notebook',
            'preco': 800.0,
            'categoria_id': [categoria.id]
        })
        #resposta
        response = self.cliente.post(
            reverse('produto-list', kwargs={'versao': 'v1'}),
            data=data,
            content_type='application/json'
        )
        #teste
        print("Detalhes resposta produto:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #usuario da ordem criada
        produto_criado = Produto.objects.get(titulo='notebook')
        #testes
        self.assertEqual(produto_criado.titulo, 'notebook')
        self.assertEqual(produto_criado.preco, 800.0)
    #
    #endregion