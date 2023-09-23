import graphene
from graphene_django import DjangoObjectType
from .models import Post,Category


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'