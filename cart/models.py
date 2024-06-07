from django.contrib.auth.models import User
from django.db.models import (
    Model,
    OneToOneField,
    DateTimeField,
    CASCADE,
    ForeignKey,
    PositiveIntegerField,
)

from product.models import Product


class Cart(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='cart')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart ({self.user.username})"


class CartItem(Model):
    cart = ForeignKey(Cart, on_delete=CASCADE, related_name='items')
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
