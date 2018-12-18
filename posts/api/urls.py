
from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	PostCreatelAPIView
	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name ='ditail'),
	url(r'^edit/(?P<pk>\d+)/$', PostUpdateAPIView.as_view(), name ='update'),
	url(r'^delete/(?P<pk>\d+)/$', PostDeleteAPIView.as_view(), name = 'delete'),
	url(r'^create/$', PostCreatelAPIView.as_view(), name='create'),
	#url(r'^get/(?P<post_id>\d+)/$', get_post, name ='get_post'),
	#url(r'^adlike/(?P<post_id>[\w-]+)/$', ad_like, name ='ad_like'),
	#url(r'^addislike/(?P<post_id>[\w-]+)/$', ad_dislike, name ='ad_dislike'),

]