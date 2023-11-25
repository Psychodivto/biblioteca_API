import graphene

from graphene_django import DjangoObjectType

from libreria.models import Libro

class LibroType(DjangoObjectType):
    class Meta:
        model = Libro
        fields = ("id", "titulo", "fecha_publicacion", "categoria", "autor")

class Query(graphene.ObjectType):
    libros = graphene.List(LibroType)

    def resolve_libros(self, info):
        return Libro.objects.all()

