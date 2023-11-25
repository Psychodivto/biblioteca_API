import graphene

import libreria.schemas.usuarios
import libreria.schemas.autores
import libreria.schemas.libros
import libreria.schemas.prestamos
import libreria.schemas.devoluciones
import libreria.schemas.reservas
import libreria.schemas.editoriales



class Query(libreria.schemas.usuarios.Query, 
            libreria.schemas.autores.Query, 
            libreria.schemas.libros.Query,
            libreria.schemas.prestamos.Query,
            libreria.schemas.devoluciones.Query,
            libreria.schemas.reservas.Query,
            libreria.schemas.editoriales.Query,
            graphene.ObjectType
):
    pass

class Mutation(libreria.schemas.usuarios.Mutation,
      graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)