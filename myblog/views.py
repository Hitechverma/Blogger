from django.shortcuts import render
from rest_framework.views import APIView
from myblog.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from myblog.serializers import *
from rest_framework.response import Response
import datetime 
from django.http import Http404

# Create your views here.


class CreateUser(APIView):
    def post(self,request,format=json):
        # print request.data
        userdata = request.data
        # print userdata['email']
        
        try:
            if user.objects.filter(email = userdata['email']):
                newdata = user.objects.filter(email = userdata['email'])
                print "USer already exist"
                print newdata.values()
                return Response(newdata.values())
                # user_check = user.objects.filter(email = "nupuratray94@gmail.com")
        except user.DoesNotExist:
            user_serializer = UserSerializers(data = userdata)
            if user_serializer.is_valid():
                user_serializer.save()
                print "yes it is working"
                return Response(user_serializer.data)
        return Response("Its outer shell")


class PostList(APIView):

    def get(self,request, format=None):
        posts = userpost.objects.all()
        serializer = PostSerializers(posts,many=True)
        # print serializer.data
        for data in serializer.data:
            old_datetime = str(data['created_at'])
            new_datetime = datetime.datetime.strptime(old_datetime,'%Y-%m-%dT%H:%M:%SZ')
            data['created_at'] = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return Response(serializer.data)

    def post(self,request, format=json):
        print "what the hell  ",request.data
        post_serializer = PostSerializers(data=request.data)
        # print "Did you say somth ", post_serializer.initial_data
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors)


class BlogList(APIView):
    """docstring for BlogList"""
    def get_object(self, pk):
        try:
            return userpost.objects.get(pk=pk)
        except userpost.DoesNotExist:
            raise Http404


    def get(self,request,pk,format=None):
        userblog = self.get_object(pk)
        thepost = PostSerializers(userblog)
        print thepost.data
        return Response(thepost.data)