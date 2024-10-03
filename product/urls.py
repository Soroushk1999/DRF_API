from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductListViewSet,
    ProductDetailViewSet,
    CategoryViewSet
)

router = DefaultRouter()
router.register('product_list', ProductListViewSet, basename='product_list')
router.register('product_detail', ProductDetailViewSet, basename='product_detail')
router.register('category', CategoryViewSet, basename='category')
app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
]
