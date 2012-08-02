"""
This code should be copy and pasted into blog/urls.py
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    ## add your url here
   #use this url or the next one..they are the same explanation.....
   # url(r'^posts/search/(\w+)$', 'blog.views.post_search'), 
    url(r'^posts/search/(?P<term>\w+)$','blog.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit/$','blog.views.edit_comment'),
)

