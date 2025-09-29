from rest_framework import serialixers
from .models import Order, OrderItem

class OrderItemSerializer(serialixers.ModelSerializer):
    menu_item_name = serialixers.CharField(source="menu_item.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ['menu_item_name', 'quantity', 'price']

class OrderSerializer(serialixers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'created_at', 'total_amount', 'items']