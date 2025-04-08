# == importacoes
import factory
from faker import Factory as FF

# django: usuario
from django.contrib.auth.models import User

# -------------------
from ordem.modelos import Ordem
from produto.fabricas import ProdutoFabrica

# cria um objeto que gera dados falsos
falsosDados = FF.create()


class UsuarioFabrica(factory.django.DjangoModelFactory):
    # atributos
    email = factory.Faker("pystr")
    username = factory.LazyAttribute(lambda x: falsosDados.name())

    # sobreescrita: polimorfismo
    @classmethod
    def _prepare(cls, create, **kwargs):
        # usuario super
        usuario = super(UsuarioFabrica, cls)._prepare(create, **kwargs)
        # senha do email
        senha = kwargs.pop("password", None)
        # tentativa 2
        if not senha:
            senha = kwargs.pop("senha", None)
        # validacao
        if senha:
            # define a senha configura nos parametros
            usuario.set_password(senha)
            # -------------------
            if create:
                usuario.save()
        # def retorno
        return usuario

    # polimorfismo: sobreescrita
    class Meta:
        model = User


class OrdemFabrica(factory.django.DjangoModelFactory):
    # atributos
    usuario = factory.SubFactory(UsuarioFabrica)
    # instancia
    produto = factory.LazyAttribute(ProdutoFabrica)

    # decorador, configura para ser executado depois que criar o objeto
    # o "**kwargs" sao parametros nao especificados convertidos p/ um dicionario, neste caso, o dicionario chamado "kwargs"
    # uso: categoria(true, true, nome='categoria', classe='tipo'), um dicionario com dois itens, chave e valor definidos
    @factory.post_generation
    def produto(self, criado, extraido, **kwargs):
        # validacao
        if not criado:
            return
        # ---------------
        if extraido:
            # loop
            for produto in extraido:
                self.produto.add(produto)

    # classes: sobreescrita
    class Meta:
        model = Ordem
        skip_postgeneration_save = True
