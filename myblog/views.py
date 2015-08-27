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

    def post(self,request, format=None):
        print "what the hell  ",request.data
        dataset = request.data
        post_serializer = PostSerializers(data=dataset,many=True)
        print "Did you say somth ", post_serializer.initial_data
        if post_serializer.is_valid(raise_exception=True):
            print post_serializer.errors
            post_serializer.save()
            print "the world", post_serializer.data, "i am    j"
            return Response(post_serializer.data)
        return Response(post_serializer.errors)