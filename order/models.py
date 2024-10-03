from django.db import models
from django.contrib.auth.models import User
from product.models import Product  # Assuming you have a products app


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ])
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in Order {self.order.id}"
