from rest_framework import viewsets, permissions
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({"detail": "Your cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=user, total_price=total_price, status='pending')

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear the cart
        cart.delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class OrderTemplateView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'order/order.html'
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'some_data': 'This is some data to pass to the template'
#         }
#         return Response(context, template_name=self.template_name)
