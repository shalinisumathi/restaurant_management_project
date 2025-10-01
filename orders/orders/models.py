from django.db import models
class Coupon(models.model):
    code = models.charField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_degits=5, decimal_place=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"