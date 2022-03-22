from django.urls import path
from . import views


app_name = 'post'




urlpatterns = [
    path('',views.PostListView.as_view(),name='post-list'),
    path('<int:pk>',views.PostDetailView.as_view(),name='post-detail'),
    path ('add_post/',views.add_post,name='add_post'),
    path ('update_post/<int:pk>',views.update_post,name='update_post'),
]