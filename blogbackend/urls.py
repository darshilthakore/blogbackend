"""blogbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from myapi import views

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# custom auth token which returns a token after login is successful
class CustomAuthToken(ObtainAuthToken):
    authentication_classes = (TokenAuthentication, )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'dob': user.userprofile.dob,
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),
    path('auth/', CustomAuthToken.as_view()),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^$', views.HomePageView.as_view()),
    re_path(r'^(?P<url>.*)/$', views.HomePageView.as_view()),
]