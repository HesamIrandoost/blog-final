from rest_framework import generics, permissions
from .serializers import PostListDetailSerializer, PostCreateUpdateSerializer
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

class AuthorListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            return PostCreateUpdateSerializer
        return PostListDetailSerializer
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile)
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user.profile)
    

class AuthorRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostCreateUpdateSerializer
    lookup_field='slug'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.profile)
    