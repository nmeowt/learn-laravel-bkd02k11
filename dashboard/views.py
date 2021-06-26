from order.serializers import OrderItemSerializer
from order.models import Order, OrderItem
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers

from django.http import HttpResponse


def order_data(request):
    order_item = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_item, many=True)
    return JsonResponse(serializer.data, safe=False)
    # dataset = []
    # for i, item in enumerate(Order.objects.all()):
    #     order_item = OrderItem.objects.filter(order=item)
    #     dataset.append(order_item)

    # return JsonResponse(list(OrderItem.objects.all().values()), safe=False)
