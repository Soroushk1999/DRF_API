from django.contrib import admin
from .models import Cart, CartItem, Product  # Ensure Product is imported


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['product']
    list_editable = ['product']

    def product_name(self, obj):
        return obj.product.name

    product_name.short_description = 'Product'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']
    inlines = [CartItemInline]

