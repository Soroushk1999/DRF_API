from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'list', CartViewSet, basename='cart')
router.register(r'items', CartItemViewSet, basename='cart-items')

app_name = 'cart'
urlpatterns = [
    path('', include(router.urls)),
]
