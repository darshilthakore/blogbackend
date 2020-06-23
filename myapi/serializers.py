from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image_url', 'owner']

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'blogs']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
