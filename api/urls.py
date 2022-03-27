from django.urls import path , include,re_path
from . import views
from django.views.generic import TemplateView


app_name = 'api'




urlpatterns = [
    path('',views.PostListApi.as_view(),name='post-list'),
    path('<int:pk>',views.PostDetailApi.as_view(),name='post-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>',views.UserDetail.as_view(),name='user-detail'),
    # path('revoke/',views.Revoke.as_view(),name='revoke')
    
   
   

]