import graphene

from graphene_django import DjangoObjectType

from libreria.models import Editorial

class EditorialType(DjangoObjectType):
    class Meta:
        model = Editorial
        fields = ("id", "nombre", "direccion", "ciudad", "telefono", "correo")

class Query(graphene.ObjectType):
    editoriales = graphene.List(EditorialType)

    def resolve_editoriales(self, info):
        return Editorial.objects.all()
