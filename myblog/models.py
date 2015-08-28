from django.db import models
import datetime


# Create your models here.
class userpost(models.Model):
    """docstring for userpost"""
    post = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.username
