from django.urls import path
from .views import *

urlpatterns = [
    path("coupon/validate/", couponValidationView.as_view(), name="coupon-validate"),
    
]