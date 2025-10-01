from django.db import models
class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])

class Order(models.model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
]
status = models.charField(max_length=20, choices=STATUS_CHOICES)
total_price = models.DecimalField(max_digits=10, decimal_places=2)
created_at = models.DateTimeField(auto_now_add=True)
objects = ActiveOrderManager

order.objects.get_active_orders().filter(total_price__gt=500)
from orders.models import order
active_orders = order . objects.get_active_orders()
print(active_orders)