from rest_framework import serializers
from myblog.models import *


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = user
        field = ('id','User_name','email','access_token')

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = userpost
        field = ('id','post', 'username', 'main')
