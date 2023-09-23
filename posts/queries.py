import graphene
from .types import PostType,CategoryType
from .models import Post,Category


class Query(object):
    posts = graphene.List(PostType)
    categories = graphene.List(CategoryType)
    active_categories = graphene.List(CategoryType)
    
    def resolve_posts(self, info):
        return Post.objects.all()
    
    def resolve_active_categories(self, info):
        return Category.objects.filter(is_active=True)
    
    def resolve_categories(self, info):
        return Category.objects.all()