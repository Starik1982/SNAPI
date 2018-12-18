from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["user", "title", "content", "date"]

	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)