from django.urls import path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include


from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'register', views.RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]