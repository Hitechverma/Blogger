from django.shortcuts import render
from rest_framework.views import APIView
from myblog.models import *
import json
from myblog.serializers import *
from rest_framework.response import Response
# Create your views here.



class PostList(APIView):

    def get(self,request, format=None):
        posts = userpost.objects.all()
        serializer = PostSerializers(posts,many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        print "what the hell  ",request.data
        # dataset = []
        # dataset['username'] = request.data['username']
        # dataset['post'] = request.data['post']
        # print "hhhhhhhhhh",dataset
        post_serializer = PostSerializers(data=request.data,many=True)
        print "Did you say somth ", post_serializer.initial_data
        if post_serializer.is_valid():
            print " kya bee ",post_serializer.validated_data
            post_serializer.save()
            print "the world", post_serializer.data, "i am    j"
            return Response(post_serializer.data)
        return Response(post_serializer.errors)