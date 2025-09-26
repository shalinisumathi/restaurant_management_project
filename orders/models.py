from django.db import models
from django.db import OrderStatus

class order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"order #{self.id} - {self.status}"
