import graphene

from graphene_django import DjangoObjectType

from libreria.models import Autor

class AutorType(DjangoObjectType):
    class Meta:
        model = Autor
        fields = ("id", "nombre", "apellido", "biografia", "nacimiento", "nacionalidad")

class Query(graphene.ObjectType):
    autores = graphene.List(AutorType)

    def resolve_autores(self, info):
        return Autor.objects.all()