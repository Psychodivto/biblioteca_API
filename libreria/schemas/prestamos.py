import graphene

from graphene_django import DjangoObjectType

from graphene import relay

from libreria.models import Prestamo

class PrestamoType(DjangoObjectType):
    class Meta:
        model = Prestamo
        fields = ("id", "libro", "usuario", "fecha_prestamo", "fecha_devolucion", "devuelto")

class PrestamoConectado(relay.Connection):
    class Meta:
        node = PrestamoType
class Query(graphene.ObjectType):
    prestamos = graphene.List(PrestamoType)
    usuarios_prestamo = graphene.Field(PrestamoType, usuario=graphene.Int())

    def resolve_prestamos(self, info, **kwargs):
        return Prestamo.objects.all()

    def resolve_usuarios_prestamo(self, info, usuario):
        return Prestamo.objects.filter(usuario=usuario)

class CreatePrestamo(graphene.Mutation):
    id = graphene.Int()
    libro = graphene.Int()
    usuario = graphene.Int()
    fecha_prestamo = graphene.Date()
    fecha_devolucion = graphene.Date()
    devuelto = graphene.Boolean()

    class Arguments:
        libro = graphene.Int()
        usuario = graphene.Int()
        fecha_prestamo = graphene.Date()
        fecha_devolucion = graphene.Date()
        devuelto = graphene.Boolean()

    def mutate(self, info, libro, usuario, fecha_prestamo, fecha_devolucion, devuelto):
        prestamo = Prestamo(libro=libro, usuario=usuario, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, devuelto=devuelto)
        prestamo.save()

        return CreatePrestamo(
            id=prestamo.id,
            libro=prestamo.libro,
            usuario=prestamo.usuario,
            fecha_prestamo=prestamo.fecha_prestamo,
            fecha_devolucion=prestamo.fecha_devolucion,
            devuelto=prestamo.devuelto
        )

class UpdatePrestamo(graphene.Mutation):
    id = graphene.Int()
    libro = graphene.Int()
    usuario = graphene.Int()
    fecha_prestamo = graphene.Date()
    fecha_devolucion = graphene.Date()
    devuelto = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        libro = graphene.Int()
        usuario = graphene.Int()
        fecha_prestamo = graphene.Date()
        fecha_devolucion = graphene.Date()
        devuelto = graphene.Boolean()

    def mutate(self, info, id, libro, usuario, fecha_prestamo, fecha_devolucion, devuelto):
        prestamo = Prestamo.objects.get(pk=id)
        prestamo.libro = libro
        prestamo.usuario = usuario
        prestamo.fecha_prestamo = fecha_prestamo
        prestamo.fecha_devolucion = fecha_devolucion
        prestamo.devuelto = devuelto
        prestamo.save()

        return UpdatePrestamo(
            id=prestamo.id,
            libro=prestamo.libro,
            usuario=prestamo.usuario,
            fecha_prestamo=prestamo.fecha_prestamo,
            fecha_devolucion=prestamo.fecha_devolucion,
            devuelto=prestamo.devuelto
        )

class DeletePrestamo(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        prestamo = Prestamo.objects.get(pk=id)
        prestamo.delete()

        return DeletePrestamo(
            id=id
        )

class Mutation(graphene.ObjectType):
    create_prestamo = CreatePrestamo.Field()
    update_prestamo = UpdatePrestamo.Field()
    delete_prestamo = DeletePrestamo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)