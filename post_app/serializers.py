from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'comments']


class UserSerializer(serializers.ModelSerializer):
    blog_posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'post']


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='author.name')
    

    class Meta:
        model = Category
        fields = ['id', 'name' ]
        