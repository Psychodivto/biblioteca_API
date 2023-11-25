import graphene

from graphene_django import DjangoObjectType

from libreria.models import Devolucion

class DevolucionType(DjangoObjectType):
    class Meta:
        model = Devolucion
        fields = ("id", "prestamo", "fecha_devolucion")

class Query(graphene.ObjectType):
    devoluciones = graphene.List(DevolucionType)

    def resolve_devoluciones(self, info):
        return Devolucion.objects.all()