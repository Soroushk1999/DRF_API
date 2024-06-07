from django.contrib import admin
from cart.admin import CartAdmin
from product.admin import ProductAdmin, CategoryAdmin


admin.site.register(CartAdmin)
admin.site.register(ProductAdmin, CategoryAdmin)
