import graphene
import posts.queries
import posts.mutations


class Query(posts.queries.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_post = posts.mutations.CreatePost.Field()
    create_category = posts.mutations.CreateCategory.Field()
    update_post = posts.mutations.UpdatePost.Field()
    delete_post = posts.mutations.DeletePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)