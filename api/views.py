# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from posts.models import Post
from .serializers import PostSerializer

# Create your views here.



class PostListApi(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
