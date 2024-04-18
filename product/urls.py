from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductDetailViewSet


router = DefaultRouter()
router.register('product_list', ProductViewSet, basename='product_list')
router.register('product_detail', ProductDetailViewSet, basename='product_detail')
app_name = 'product'
urlpatterns = [
    path('api/', include(router.urls)),
]
