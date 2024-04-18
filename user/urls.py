from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-profiles', UserProfileViewSet)
app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
