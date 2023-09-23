import graphene
from .types import PostType,CategoryType
from .models import Post,Category


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String()
        category = graphene.Int()
    post = graphene.Field(PostType)

    def mutate(self, info, title, content=None,category=None):
        post = Post(title=title, content=content,category=category)
        post.save()
        return CreatePost(post=post)

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)

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