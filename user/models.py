from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'user_profile'
