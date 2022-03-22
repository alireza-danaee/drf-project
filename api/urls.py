from django.urls import path
from . import views


app_name = 'api'




urlpatterns = [
    path('',views.PostListApi.as_view(),name='post-list'),
    path('<int:pk>',views.PostDetailApi.as_view(),name='post-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>',views.UserDetail.as_view(),name='user-detail'),
   

]