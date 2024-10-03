from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return [cart]


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        product_id = serializer.validated_data.get('product_id')
        quantity = serializer.validated_data.get('quantity')

        # Check if the item already exists in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

        if not created:
            # If it exists, update the quantity
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # Save new cart item
            serializer.save(cart=cart)

    def perform_update(self, serializer):
        cart = self.get_queryset()
        serializer.save(cart=cart)
