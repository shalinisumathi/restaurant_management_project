from rest_framework.generics import ListAPIView
from .models import 
from .serializers import MenuCategorySerializer
class MenuCategorySerializerView(ListAPIView):
    queryset = MenuCategory .objects.all()
    serializer_class = MenuCategorySerializer

