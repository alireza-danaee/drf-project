from django.urls import path , include,re_path
from .views import UserViewSet,PostViewSet
from django.views.generic import TemplateView
from rest_framework import routers


app_name = 'api'




router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)


urlpatterns = [
    path('' , include(router.urls))
]