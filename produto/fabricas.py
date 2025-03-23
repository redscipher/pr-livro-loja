#== importacoes
import factory
#modelos
from produto.modelos import Produto, Categoria

#categoria
class CategoriaFabrica(factory.django.DjangoModelFactory):
    #atributos
    titulo = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    descricao = factory.Faker('pystr')
    ativo = factory.Iterator([True, False])

    #== classes
    #herdadas: sobreescrita
    class Meta:
        model = Categoria

#produto
class ProdutoFabrica(factory.django.DjangoModelFactory):
    #atributos
    preco = factory.Faker('pyint')
    titulo = factory.Faker('pystr')
    #instancia
    categoria = factory.LazyAttribute(CategoriaFabrica)

    #decorador, configura para ser executado depois que criar o objeto
    # o "**kwargs" sao parametros nao especificados convertidos p/ um dicionario, neste caso, o dicionario chamado "kwargs"
    # uso: categoria(true, true, nome='categoria', classe='tipo'), um dicionario com dois itens, chave e valor definidos
    @factory.post_generation
    def categoria(self, criada, extraida, **kwargs):
        #validacao
        if not criada:
            return
        #-----------------
        if extraida:
            #loop
            for categoria in extraida:
                self.categoria.add(categoria)
                
    #== classes
    #polimorfismo
    class Meta:
        model = Produto
        skip_postgeneration_save=True