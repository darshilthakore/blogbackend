from django.shortcuts import render
from django.views.generic import TemplateView


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import permissions
from myapi.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


from .serializers import UserSerializer, BlogSerializer, RegisterSerializer
from .models import Blog, UserProfile

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]