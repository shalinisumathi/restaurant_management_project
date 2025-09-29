from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemVIewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemVIewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]