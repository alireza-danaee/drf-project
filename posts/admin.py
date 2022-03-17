from django.contrib import admin
from .models import Post
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('text','author','status','created','updated')
    list_filter = ('status','created','author')
    

admin.site.register(Post,AdminPost)
