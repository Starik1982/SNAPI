from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',
		'user',
		'like',
		'dislike',
		'id',		
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',
		'user',
		'like',
		'dislike',
		'id',		
		]

class PostUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',
		]

class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',	
		]