import graphene

from graphene_django import DjangoObjectType

from graphene import relay

from libreria.models import Devolucion

class DevolucionType(DjangoObjectType):
    class Meta:
        model = Devolucion
        fields = ("id", "prestamo", "fecha_devolucion")


class DevolucionConectado(relay.Connection):
    class Meta:
        node = DevolucionType

class Query(graphene.ObjectType):
    all_devoluciones = graphene.List(DevolucionType)

    def resolve_devoluciones(self, info, **kwargs):
        return Devolucion.objects.all()

class CreateDevolucion(graphene.Mutation):
    id = graphene.Int()
    prestamo = graphene.Int()
    fecha_devolucion = graphene.Date()

    class Arguments:
        prestamo = graphene.Int()
        fecha_devolucion = graphene.Date()

    def mutate(self, info, prestamo, fecha_devolucion):
        devolucion = Devolucion(prestamo=prestamo, fecha_devolucion=fecha_devolucion)
        devolucion.save()

        return CreateDevolucion(
            id=devolucion.id,
            prestamo=devolucion.prestamo,
            fecha_devolucion=devolucion.fecha_devolucion
        )

class UpdateDevolucion(graphene.Mutation):
    id = graphene.Int()
    prestamo = graphene.Int()
    fecha_devolucion = graphene.Date()

    class Arguments:
        id = graphene.Int()
        prestamo = graphene.Int()
        fecha_devolucion = graphene.Date()

    def mutate(self, info, id, prestamo, fecha_devolucion):
        devolucion = Devolucion.objects.get(pk=id)
        devolucion.prestamo = prestamo
        devolucion.fecha_devolucion = fecha_devolucion
        devolucion.save()

        return UpdateDevolucion(
            id=devolucion.id,
            prestamo=devolucion.prestamo,
            fecha_devolucion=devolucion.fecha_devolucion
        )

class DeleteDevolucion(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        devolucion = Devolucion.objects.get(pk=id)
        devolucion.delete()

        return DeleteDevolucion(
            id=id
        )

class Mutation(graphene.ObjectType):
    create_devolucion = CreateDevolucion.Field()
    update_devolucion = UpdateDevolucion.Field()
    delete_devolucion = DeleteDevolucion.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)