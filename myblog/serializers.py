from rest_framework import serializers
from myblog.models import *

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = userpost
        field = ('post', 'username')