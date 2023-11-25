import graphene

from graphene_django import DjangoObjectType

from libreria.models import Prestamo

class PrestamoType(DjangoObjectType):
    class Meta:
        model = Prestamo
        fields = ("id", "libro", "usuario", "fecha_prestamo", "fecha_devolucion", "devuelto")

class Query(graphene.ObjectType):
    prestamos = graphene.List(PrestamoType)

    def resolve_prestamos(self, info):
        return Prestamo.objects.all()
        