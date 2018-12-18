
from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	get_post,
	post_update,
	post_delete,
	ad_like,
	ad_dislike,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create, name='create'),
	url(r'^get/(?P<post_id>\d+)/$', get_post, name ='get_post'),
	url(r'^edit/(?P<id>\d+)/$', post_update, name ='post_update'),
	url(r'^delete/(?P<post_id>[\w-]+)/$', post_delete),
	url(r'^adlike/(?P<post_id>[\w-]+)/$', ad_like, name ='ad_like'),
	url(r'^addislike/(?P<post_id>[\w-]+)/$', ad_dislike, name ='ad_dislike'),

]