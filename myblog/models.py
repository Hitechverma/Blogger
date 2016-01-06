from django.db import models
import datetime


# Create your models here.

class user(models.Model):
    User_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    access_token = models.CharField(max_length=400)

    def __str__(self):
        return self.User_name


class userpost(models.Model):
    """docstring for userpost"""
    post = models.CharField(max_length=200)
    username = models.ForeignKey(user)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.username


