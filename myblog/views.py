from django.shortcuts import render
from rest_framework.views import APIView
from myblog.models import *
from myblog.serializers import *
from rest_framework.response import Response
# Create your views here.



class PostList(APIView):

    def get(self,request, format=None):
        posts = userpost.objects.all()
        serializer = PostSerializers(posts,many=True)
        return Response(serializer.data)