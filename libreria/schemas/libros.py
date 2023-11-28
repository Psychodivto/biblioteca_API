import graphene

from graphene_django import DjangoObjectType

from graphene import relay
from libreria.models import Libro

class LibroType(DjangoObjectType):
    class Meta:
        model = Libro
        fields = ("id", "titulo", "fecha_publicacion", "categoria", "autor")

class LibroConectado(relay.Connection):
    class Meta:
        node = LibroType
class Query(graphene.ObjectType):
    all_libros = graphene.List(LibroType)
    nombre_libro = graphene.Field(LibroType, titulo=graphene.String())
    categoria_libro = graphene.Field(LibroType, categoria=graphene.String())

    def resolve_libros(self, info, **kwargs):
        return Libro.objects.all()

    def resolve_nombre_libro(self, info, titulo):
        return Libro.objects.filter(titulo=titulo)

    def resolve_categoria_libro(self, info, categoria):
        return Libro.objects.filter(categoria=categoria)

class CreateLibro(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    fecha_publicacion = graphene.Date()
    categoria = graphene.String()
    autor = graphene.Int()

    class Arguments:
        titulo = graphene.String()
        fecha_publicacion = graphene.Date()
        categoria = graphene.String()
        autor = graphene.Int()

    def mutate(self, info, titulo, fecha_publicacion, categoria, autor):
        libro = Libro(titulo=titulo, fecha_publicacion=fecha_publicacion, categoria=categoria, autor=autor)
        libro.save()

        return CreateLibro(
            id=libro.id,
            titulo=libro.titulo,
            fecha_publicacion=libro.fecha_publicacion,
            categoria=libro.categoria,
            autor=libro.autor
        )

class UpdateLibro(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    fecha_publicacion = graphene.Date()
    categoria = graphene.String()
    autor = graphene.Int()

    class Arguments:
        id = graphene.Int()
        titulo = graphene.String()
        fecha_publicacion = graphene.Date()
        categoria = graphene.String()
        autor = graphene.Int()

    def mutate(self, info, id, titulo, fecha_publicacion, categoria, autor):
        libro = Libro.objects.get(pk=id)
        libro.titulo = titulo
        libro.fecha_publicacion = fecha_publicacion
        libro.categoria = categoria
        libro.autor = autor
        libro.save()

        return UpdateLibro(
            id=libro.id,
            titulo=libro.titulo,
            fecha_publicacion=libro.fecha_publicacion,
            categoria=libro.categoria,
            autor=libro.autor
        )

class DeleteLibro(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        libro = Libro.objects.get(pk=id)
        libro.delete()

        return DeleteLibro(
            id=id
        )

class Mutation(graphene.ObjectType):
    create_libro = CreateLibro.Field()
    update_libro = UpdateLibro.Field()
    delete_libro = DeleteLibro.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)