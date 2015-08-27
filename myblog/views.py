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
        try:
            serializer = PostSerializers(data=request.data,many=True)
            print "Did you say somth ", serializer
            if serializer.isValid():
                serializer.save()
                pos = userpost.objects.get(username=request.data['username'])
                print pos
                return Response(serializer.data)
            return Response(serializer.errors)
        except :
            print "Except"
            return Response("Not working")

