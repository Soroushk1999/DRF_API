from django.urls import path, include
from django.contrib.auth import views

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserProfileViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'register', UserViewSet)
router.register(r'user-profile', UserProfileViewSet, basename='user-profile')
router.register(r'login', LoginViewSet, basename='login')

app_name = 'user'
urlpatterns = [
    path('', include(router.urls)),
]
