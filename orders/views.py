from rest _framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get("code")
        if not code:
            return Response({"error": "Coupon code is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            Coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            return Response({"error": "Invalid coupon code"}, status=status.HTTP_400_BAD_REQUEST)
        today = timezone.now().date()

        if not coupon.is_active:
            return Response({"error": "Coupon is not active"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not (coupon.valid_from <= today <= coupon.valid_until):
            return Response({"error": "coupon is expired or not yet valid"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "success": True,
            "code": coupon.code
            "discound_percentage": float(coupon.discound_percentage)
        }, status=status.HTTP_200_OK)