from django.conf.urls import url
from django.contrib import admin

from .views import UserCreateAPI

urlpatterns = [
	url(r'^register/$', UserCreateAPI.as_view(), name='register'),


]