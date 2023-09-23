import graphene
from .types import PostType
from .models import Post


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, content=None):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, **kwargs):
        post = Post.objects.get(id=id)
        for key, value in kwargs.items():
            if value is not None:
                setattr(post, key, value)
        post.save()
        return UpdatePost(post=post)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        Post.objects.filter(id=id).delete()
        return DeletePost(success=True)