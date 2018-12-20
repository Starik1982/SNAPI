from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	PostCreatelAPIView,
	PostLikeView,

	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name ='ditail'),
	url(r'^edit/(?P<pk>\d+)/$', PostUpdateAPIView.as_view(), name ='update'),
	url(r'^like/(?P<pk>\d+)/$', PostLikeView.as_view(), name ='like'),
	url(r'^delete/(?P<pk>\d+)/$', PostDeleteAPIView.as_view(), name = 'delete'),	
	url(r'^create/$', PostCreatelAPIView.as_view(), name='create'),
]