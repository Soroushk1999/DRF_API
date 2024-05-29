from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock_quantity = models.IntegerField(default=0)
    description = models.TextField(default='')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title
