from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class user(models.Model):
    User_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    access_token = models.CharField(max_length=400)

    def __str__(self):
        return self.User_name


class userpost(models.Model):
    """docstring for userpost"""
    post = models.CharField(max_length=2000)
    post_title = models.CharField(max_length=500, default="blog")
    username = models.ForeignKey(user)
    created_at = models.DateTimeField(default=timezone.now())
    main = models.CharField(max_length=100, default="NO_name")

    def __str__(self):
        return self.username.User_name

class comment(models.Model):
    """docstring for comment"""
    blogid = models.ForeignKey(userpost)
    author = models.ForeignKey(user)
    comment_data = models.CharField(max_length = 200)
    comment_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.comment_data
        

