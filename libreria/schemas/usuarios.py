import graphene

from graphene import relay

from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password")

class Query(graphene.ObjectType):
    users = graphene.Field(UserType, id=graphene.Int(required=True))
    all_users = graphene.List(UserType)


    def resolve_users(self, info):
        users = info.context.user
        if users.is_anonymous:
            raise Exception('Not logged in!')

        return get_user_model().objects.all()

class CreateUser(graphene.Mutation):
    all_user = graphene.Field(UserType)
    

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, email, password):
        user = get_user_model()(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class delete_user(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        user = get_user_model().objects.get(id=id)
        user.delete()

        return delete_user(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = delete_user.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


