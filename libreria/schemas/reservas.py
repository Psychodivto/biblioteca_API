import graphene

from graphene_django import DjangoObjectType

from django import relay

from libreria.models import Reserva

class ReservaType(DjangoObjectType):
    class Meta:
        model = Reserva
        fields = ("id", "libro", "usuario", "fecha_reserva")

class Query(graphene.ObjectType):
    all_reservas = graphene.List(ReservaType)
    usuario_reservas = graphene.Field(ReservaType, usuario=graphene.Int())

    def resolve_reservas(self, info, **kwargs):
        return Reserva.objects.all()

    def resolve_usuarios_reservas(self, info, usuario):
        return Reserva.objects.filter(usuario=usuario)

class CreateReserva(graphene.Mutation):
    id=graphene.Int()
    libro=graphene.Int()
    usuario=graphene.Int()
    fecha_reserva=graphene.Date()

class Arguments:
    libro=graphene.Int()
    usuario=graphene.Int()
    fecha_reserva=graphene.Date()

    def mutate(self, info, libro, usuario, fecha_reserva):
        reserva = Reserva(libro=libro, usuario=usuario, fecha_reserva=fecha_reserva)
        reserva.save()

        return CreateReserva(
            id=reserva.id,
            libro=reserva.libro,
            usuario=reserva.usuario,
            fecha_reserva=reserva.fecha_reserva
        )

class UpdateReserva(graphene.Mutation):
    id=graphene.Int()
    libro=graphene.Int()
    usuario=graphene.Int()
    fecha_reserva=graphene.Date()

class Arguments:
    libro=graphene.Int()
    usuario=graphene.Int()
    fecha_reserva=graphene.Date()

    def mutate(self, info, libro, usuario, fecha_reserva):
        reserva = Reserva(libro=libro, usuario=usuario, fecha_reserva=fecha_reserva)
        reserva.save()

        return UpdateReserva(
            id=reserva.id,
            libro=reserva.libro,
            usuario=reserva.usuario,
            fecha_reserva=reserva.fecha_reserva
        )

class DeleteReserva(graphene.Mutation):
    id=graphene.Int()

class Arguments:
    id=graphene.Int()

    def mutate(self, info, id):
        reserva = Reserva.objects.get(pk=id)
        reserva.delete()

        return DeleteReserva(
            id=reserva.id
        )

class Mutation(graphene.ObjectType):
    create_reserva = CreateReserva.Field()
    update_reserva = UpdateReserva.Field()
    delete_reserva = DeleteReserva.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

        