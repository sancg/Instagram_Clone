from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # When a User is deleted all their post are deleted too
    created = models.DateTimeField(auto_now_add=True)  # Timestamp
    modified = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  # Timestamp
    modified = models.DateTimeField(auto_now=True)
