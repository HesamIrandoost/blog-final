from rest_framework import generics, permissions
from .serializers import PostListDetailSerializer
from Blog.models import Post

class PostListView(generics.ListAPIView):
    serializer_class = PostListDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.filter(status=True)  

    
class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostListDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    queryset = Post.objects.filter(status=True)  