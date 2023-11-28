import graphene

from graphene_django import DjangoObjectType

from graphene import relay

from libreria.models import Editorial

class EditorialType(DjangoObjectType):
    class Meta:
        model = Editorial
        fields = ("id", "nombre", "direccion", "ciudad", "telefono", "correo")

class EditorialConectado(relay.Connection):
    class Meta:
        node = EditorialType

class Query(graphene.ObjectType):
    all_editoriales = graphene.List(EditorialType)
    nombre_editorial = graphene.Field(EditorialType, nombre=graphene.String())

    def resolve_editoriales(self, info):
        return Editorial.objects.all()

class CreateEditorial(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    direccion = graphene.String()
    ciudad = graphene.String()
    telefono = graphene.String()
    correo = graphene.String()

    class Arguments:
        nombre = graphene.String()
        direccion = graphene.String()
        ciudad = graphene.String()
        telefono = graphene.String()
        correo = graphene.String()

    def mutate(self, info, nombre, direccion, ciudad, telefono, correo):
        editorial = Editorial(nombre=nombre, direccion=direccion, ciudad=ciudad, telefono=telefono, correo=correo)
        editorial.save()

        return CreateEditorial(
            id=editorial.id,
            nombre=editorial.nombre,
            direccion=editorial.direccion,
            ciudad=editorial.ciudad,
            telefono=editorial.telefono,
            correo=editorial.correo
        )

class UpdateEditorial(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    direccion = graphene.String()
    ciudad = graphene.String()
    telefono = graphene.String()
    correo = graphene.String()

    class Arguments:
        id = graphene.Int()
        nombre = graphene.String()
        direccion = graphene.String()
        ciudad = graphene.String()
        telefono = graphene.String()
        correo = graphene.String()

    def mutate(self, info, id, nombre, direccion, ciudad, telefono, correo):
        editorial = Editorial.objects.get(pk=id)
        editorial.nombre = nombre
        editorial.direccion = direccion
        editorial.ciudad = ciudad
        editorial.telefono = telefono
        editorial.correo = correo
        editorial.save()

        return UpdateEditorial(
            id=editorial.id,
            nombre=editorial.nombre,
            direccion=editorial.direccion,
            ciudad=editorial.ciudad,
            telefono=editorial.telefono,
            correo=editorial.correo
        )

class DeleteEditorial(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        editorial = Editorial.objects.get(pk=id)
        editorial.delete()

        return DeleteEditorial(
            id=id
        )

class Mutation(graphene.ObjectType):
    create_editorial = CreateEditorial.Field()
    update_editorial = UpdateEditorial.Field()
    delete_editorial = DeleteEditorial.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)