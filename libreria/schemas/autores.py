import graphene

from graphene_django import DjangoObjectType

from graphene import relay

from libreria.models import Autor



class AutorType(DjangoObjectType):
    class Meta:
        model = Autor
        fields = ("id", "nombre", "apellido", "biografia", "nacimiento", "nacionalidad")

class AutorConectado(relay.Connection):
    class Meta:
        node = AutorType

class Query(graphene.ObjectType):
    all_autores = graphene.List(AutorType)

    def resolve_autores(self, info, **kwargs):
        return Autor.objects.all()

class CreateAutor(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    apellido = graphene.String()
    biografia = graphene.String()
    nacimiento = graphene.Date()
    nacionalidad = graphene.String()

    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        biografia = graphene.String()
        nacimiento = graphene.Date()
        nacionalidad = graphene.String()

    def mutate(self, info, nombre, apellido, biografia, nacimiento, nacionalidad):
        autor = Autor(nombre=nombre, apellido=apellido, biografia=biografia, nacimiento=nacimiento, nacionalidad=nacionalidad)
        autor.save()

        return CreateAutor(
            id=autor.id,
            nombre=autor.nombre,
            apellido=autor.apellido,
            biografia=autor.biografia,
            nacimiento=autor.nacimiento,
            nacionalidad=autor.nacionalidad
        )

class UpdateAutor(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    apellido = graphene.String()
    biografia = graphene.String()
    nacimiento = graphene.Date()
    nacionalidad = graphene.String()

    class Arguments:
        id = graphene.Int()
        nombre = graphene.String()
        apellido = graphene.String()
        biografia = graphene.String()
        nacimiento = graphene.Date()
        nacionalidad = graphene.String()

    def mutate(self, info, id, nombre, apellido, biografia, nacimiento, nacionalidad):
        autor = Autor.objects.get(pk=id)
        autor.nombre = nombre
        autor.apellido = apellido
        autor.biografia = biografia
        autor.nacimiento = nacimiento
        autor.nacionalidad = nacionalidad
        autor.save()

        return UpdateAutor(
            id=autor.id,
            nombre=autor.nombre,
            apellido=autor.apellido,
            biografia=autor.biografia,
            nacimiento=autor.nacimiento,
            nacionalidad=autor.nacionalidad
        )

class DeleteAutor(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        autor = Autor.objects.get(pk=id)
        autor.delete()

        return DeleteAutor(
            id=id
        )
    
class Mutation(graphene.ObjectType):
    create_autor = CreateAutor.Field()
    update_autor = UpdateAutor.Field()
    delete_autor = DeleteAutor.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)