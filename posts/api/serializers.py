from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	)

from posts.models import Post


class PostListSerializer(ModelSerializer):
	user = SerializerMethodField()
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
	def get_user(self, obj):
		return  str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'user',
        ]
    def get_user(self, obj):
        return  str(obj.user.username)



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

class PostLikeSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'like',
		
		]