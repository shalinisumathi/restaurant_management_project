from rest_framework import viewsets, status
from rest_framework.response import Response 
from rest_framework.permissions import IsAdminUser
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.views import APIView


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            return [IsAdminUser()]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MenuItemsByCategoryView(APIView):
    def get(self, request):
        category = request.query_params.get("category", None)

        if not category:
            return Response(
                {"error": "Category parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        items = MenuItem.objects.filter(category__iexact=category, is_available=True)

        if not items.exists():
            return Response(
                {"message": f"No menu items found in category '{category}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)