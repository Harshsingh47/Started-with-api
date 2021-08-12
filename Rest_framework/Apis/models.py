from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    video = models.FileField(upload_to='media')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.author
