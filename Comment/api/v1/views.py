# Comment/api/v1/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Comment.models import Comment
from Blog.models import Post
from .serializers import (
    CommentListSerializer, 
    CommentCreateSerializer, 
    AdminCommentUpdateSerializer
)


class PostCommentListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentListSerializer
    
    def get_queryset(self):
        post_slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=post_slug, status=True)
        return Comment.objects.filter(post=post, status=True).order_by('-created_at')
    
    def perform_create(self, serializer):
        post_slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=post_slug, status=True)
                
        serializer.save(
            user=self.request.user.profile,
            post=post
        )

class AdminCommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all().order_by('-created_at')

class AdminCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'
    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return AdminCommentUpdateSerializer
    queryset = Comment.objects.all()
    