from django.urls import path , include
from .views import PostViewSet , UserViewSet , AuthorView
from django.views.generic import TemplateView
from rest_framework import routers


app_name = 'api'




router = routers.SimpleRouter()
router.register('users', UserViewSet ,basename="users")
router.register('posts', PostViewSet , basename="posts")


urlpatterns = [
    path('' , include(router.urls)),
    path('authors/<int:pk>/' , AuthorView.as_view() ,name="author-detail")
]