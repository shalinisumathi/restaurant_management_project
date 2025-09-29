from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemVIewSet
from .views import MenuItemsByCategoryView


router = DefaultRouter()
router.register(r'menu-items', MenuItemVIewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns1 = [
    path('menu-items/by-category/', MenuItemsByCategoryView.as_view(), name='menu-items-by-category'),
]