from django.urls import path
from . import views


app_name = 'post'




urlpatterns = [
    path('',views.home,name='home'),
    path ('add_post/',views.add_post,name='add_post'),
    path ('update_post/<int:pk>',views.update_post,name='update_post'),
]