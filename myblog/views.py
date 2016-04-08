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
        blog_content = request.data['post']
        self.string_ops(str(blog_content))
        post_serializer = PostSerializers(data=request.data)
        # print "Did you say somth ", post_serializer.initial_data
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors)

    def string_ops(self,text):
        print text
        hash_list = []
        text_list = text.split(' ')
        print text_list
        for word in text_list:
            if '#' in word:
                hash_list.append(word)
        print hash_list

        # if '#' in text:
        #     print "Yesss"
        # else:
        #     print "Noooooooo"

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
        # print thepost.data
        my_dict = {}
        my_dict = thepost.data
        print my_dict
        comments = comment.objects.filter(blogid=pk)
        # print comments
        comment_list = []  #converting comment into list
        for comm in comments:
            comment_list.append(str(comm))
        print comment_list
        if comment_list:
            my_dict.update({'has_comment':True})
            my_dict.update({'comments':comment_list}) #created a dict and append a list of comment into it
            print my_dict
        return Response(my_dict)

class CommentList(APIView):
    """docstring for CommnetList"""
    def post(self,request, pk, format = json):
        print "\n SOMETHING IS COMMING \n"
        print request.data
        comment_serializer = CommentSerializers(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            print "\nHULLLLAAAAA\n\n\n"
            return Response("its working")
        return Response(comment_serializer.errors)

    def get(self,request,pk,format=None):
        comments = comment.objects.filter(blogid=pk)
        print comments
        return Response("d0ne")
        