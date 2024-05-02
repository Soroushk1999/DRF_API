from django.urls import path, include
from .views import index, under_construction

app_name = 'base'
urlpatterns = [
    path('', index, name='index'),
    path('about/', under_construction, name='about'),
    path('contact/', under_construction, name='contact'),
    path('refund/', under_construction, name='refund'),
    path('terms/', under_construction, name='terms'),

    path('orders/', under_construction, name='orders'),
    path('cart/', under_construction, name='cart'),
    path('checkout/', under_construction, name='checkout'),
]
