# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from posts.models import Post
from .serializers import PostSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperUserOrIsStaffReadOnly

# Create your views here.



class PostListApi(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = "slug"
    permission_classes = (IsAuthorOrReadOnly,)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrIsStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)








