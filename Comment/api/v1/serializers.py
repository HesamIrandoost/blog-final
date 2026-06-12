# Comment/api/v1/serializers.py
from rest_framework import serializers
from Comment.models import Comment

class CommentListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    post_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = [
            'pk',           # حتماً نیازه برای ویرایش/حذف
            'post',
            'post_title',   # عنوان پست برای نمایش
            'user',
            'author_name', 
            'author_username',
            'text',
            'status',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'status']
    
    def get_author_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_author_username(self, obj):
        return obj.user.user.username 
    
    def get_post_title(self, obj):
        return obj.post.title


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'text']
    
    def validate_post(self, value):
        if not value.status:
            raise serializers.ValidationError("This post is not available for commenting.")
        return value
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class AdminCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'text', 'status']
    
    def validate_post(self, value):
        if not value.status:
            raise serializers.ValidationError("This post is not available for commenting.")
        return value
    

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.text = validated_data.get('text', instance.text)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
