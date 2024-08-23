from rest_framework import serializers
from .models import Tag, Category, Comment, MList, Image, Album
from django.contrib.auth import get_user_model

User = get_user_model()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'mlist']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

class MListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = MList
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    album = serializers.StringRelatedField()

    class Meta:
        model = Image
        fields = ['uuid', 'url', 'thumb_url', 'user', 'size', 'album']

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['uuid', 'name', 'user', 'images']