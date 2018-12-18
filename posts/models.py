from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import auth

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank = True, null = True, default = None)
    date = models.DateField(auto_now_add=True, auto_now=False)
    like = models.IntegerField(default = 0)
    like_id = models.TextField(blank = True, null = True, default = "0 ")
    dislike = models.IntegerField(default = 0)
    dislike_id = models.TextField(blank = True, null = True, default = "0 ")

    def __str__(self):
        return "%s, %s" % (self.title, self.date)



