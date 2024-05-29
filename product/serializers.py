from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'short_description']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'stock_quantity', 'description']
