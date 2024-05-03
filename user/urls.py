from django.urls import path, include
from django.contrib.auth import views

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserProfileViewSet, LoginViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'login', LoginViewSet, basename='login')

app_name = 'user'
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
