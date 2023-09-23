from http.client import ResponseNotReady
import json
from os import stat
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from posts.models import Post
from posts.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt


class list_posts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class create_post(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class update_post(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class delete_post(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer