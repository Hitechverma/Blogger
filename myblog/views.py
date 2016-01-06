from django.shortcuts import render
from rest_framework.views import APIView
from myblog.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from myblog.serializers import *
from rest_framework.response import Response
# Create your views here.


class CreateUser(APIView):
    def post(self,request,format=json):
        print request.data
        return Response("its over")


class PostList(APIView):

    def get(self,request, format=None):
        posts = userpost.objects.all()
        serializer = PostSerializers(posts,many=True)
        return Response(serializer.data)

    def post(self,request, format=json):
        # print "what the hell  ",request.data
        post_serializer = PostSerializers(data=request.data)
        # print "Did you say somth ", post_serializer.initial_data
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors)