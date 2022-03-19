from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Post(models.Model):
    STATUS_CHOICES = (
        ('pub' , 'Published'),
        ('drf' , 'draft'),
    )
    text = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
