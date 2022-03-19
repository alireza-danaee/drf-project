from django.urls import path
from . import views


app_name = 'api'




urlpatterns = [
    path('',views.PostListApi.as_view(),name='home'),

]