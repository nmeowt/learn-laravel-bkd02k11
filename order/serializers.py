from store.serializers import ProductSerializer
from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('staff', 'code')


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'price', 'quantity')
