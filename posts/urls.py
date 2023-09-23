from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from posts import views

urlpatterns = [
    # posts
    path("posts/", views.list_posts.as_view()),
    path("posts/create/", views.create_post.as_view()),
    path("posts/update/<int:pk>/", views.update_post.as_view()),
    path("posts/delete/<int:pk>/", views.delete_post.as_view()),
]