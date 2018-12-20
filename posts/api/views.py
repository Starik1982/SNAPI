from django.shortcuts import get_object_or_404, redirect
from rest_framework import status

from rest_framework.generics import(
	ListAPIView, 				
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView,
	) 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from posts.api.serializers import (
	PostListSerializer,
	PostDetailSerializer,
	PostUpdateSerializer,
	PostCreateSerializer,
	PostLikeSerializer,

	)
from .permissions import IsOwnerOrReadOnly
from posts.models import Post


class PostCreatelAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikeView(APIView):
	def like(self, request, pk = 47):
		queryset = get_object_or_404(Post, pk=pk)
		queryset.like = queryset.like + 1
		queryset.save()
		serializer = PostLikeSerializer(queryset)
		print('this is queryset ' + str(queryset.like))
		return Response(serializer.data)






