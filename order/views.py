from order.serializers import OrderItemSerializer
from django.shortcuts import render
from .models import Order, OrderItem
from cart.cart import Cart
from datetime import date
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def order_create(request, *args, **kwargs):
    cart = Cart(request)
    today = date.today()
    num_in_day = Order.objects.filter(created__year=today.year,
                                      created__month=today.month, created__day=today.day).count()
    code = today.strftime('%Y%m%d')+str(num_in_day+1).zfill(4)
    if cart.count() > 0:
        order = Order()
        order.staff = request.user
        order.code = code
        order.save()
        for item in cart:
            order_item = OrderItem()
            order_item.order = order
            order_item.product = item['product']
            order_item.price = item['price']
            order_item.quantity = item['quantity']
            order_item.save()
    order_item = OrderItem.objects.filter(order=order)
    serializer = OrderItemSerializer(order_item, many=True)
    # cart.clear()
    return Response(serializer.data)
