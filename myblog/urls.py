from django.conf.urls import patterns, url, include
from myblog import views

from django.contrib import admin

urlpatterns = [
    url(r'^posts/$',views.PostList.as_view()),
    url(r'^user/$',views.CreateUser.as_view()),
    url(r'^blogs/(?P<pk>[0-9]+)/$',views.BlogList.as_view())
    # url(r'^comment/(?P<pk>[0-9]+)$',views)
]