import graphene
from .types import PostType
from .models import Post


class Query(object):
    all_posts = graphene.List(PostType)
    
    def resolve_all_posts(self, info):
        return Post.objects.all()