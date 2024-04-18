from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer, ProductDetailSerializer
from .models import Product, ProductDetail


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    pagination_class = PageNumberPagination


