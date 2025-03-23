#== importacoes
import factory
#django: usuario
from django.contrib.auth.models import User
#-------------------
from ordem.modelos import Ordem
from produto.fabricas import ProdutoFabrica

class UsuarioFabrica(factory.django.DjangoModelFactory):
    #atributos
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
    
    #polimorfismo: sobreescrita
    class Meta:
        model = User
        
class OrdemFabrica(factory.django.DjangoModelFactory):
    #atributos
    usuario = factory.SubFactory(UsuarioFabrica)
    #instancia
    produto = factory.LazyAttribute(ProdutoFabrica)
    
    #decorador, configura para ser executado depois que criar o objeto
    # o "**kwargs" sao parametros nao especificados convertidos p/ um dicionario, neste caso, o dicionario chamado "kwargs"
    # uso: categoria(true, true, nome='categoria', classe='tipo'), um dicionario com dois itens, chave e valor definidos
    @factory.post_generation
    def produto(self, criado, extraido, **kwargs):
        #validacao
        if not criado:
            return
        #---------------
        if extraido:
            #loop
            for produto in extraido:
                self.produto.add(produto) 
    
    #classes: sobreescrita
    class Meta:
        model = Ordem