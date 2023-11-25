import graphene

from graphene_django import DjangoObjectType

from libreria.models import Reserva

class ReservaType(DjangoObjectType):
    class Meta:
        model = Reserva
        fields = ("id", "libro", "usuario", "fecha_reserva")

class Query(graphene.ObjectType):
    reservas = graphene.List(ReservaType)

    def resolve_reservas(self, info):
        return Reserva.objects.all()
        