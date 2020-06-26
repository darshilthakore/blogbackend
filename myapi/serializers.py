from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, UserProfile

#blog serializer
class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image_url', 'owner']

#user serializer
class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())
    dob = serializers.DateField(source='userprofile.dob')
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'blogs', 'dob']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id',read_only=True)
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(source="user.password")
    email = serializers.CharField(source="user.email")
    class Meta:
        model = UserProfile
        fields = ['id','username','password', 'email', 'dob']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)

        print(f"user data {user_data}")
        print(validated_data)
        userprofile = UserProfile.objects.create(user=user, **validated_data)
        userprofile.save()
        # user = User.objects.create_user()
        return userprofile
