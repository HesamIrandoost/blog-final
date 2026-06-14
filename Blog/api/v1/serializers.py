from Blog.models import Post, Category
from rest_framework import serializers


class PostListDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "author_name",
            "author_username",
            "slug",
            "title",
            "cover",
            "content",
            "category",
            "status",
            "created_at",
            "updated_at",
        ]

    def get_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_author_username(self, obj):
        return obj.author.user.username

    def get_category(self, obj):
        return obj.category.slug


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "slug",
            "title",
            "cover",
            "content",
            "category",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    posts = PostListDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["name", "posts"]
        # read_only_fields=
