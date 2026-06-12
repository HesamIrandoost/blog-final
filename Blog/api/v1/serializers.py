from Blog.models import Post
from rest_framework import serializers


class PostListDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()    
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
        'author_name', 'author_username', 
        'slug', 'title',
        'cover', 'content', 'category',
        'status', 'created_at', 'updated_at'
        ]

    def get_author_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'

    def get_author_username(self, obj):
        return obj.author.user.username
    

class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        