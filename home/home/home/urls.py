from django.urls import path  
from .views import TableDetailView

urlpatterns = [
    path("api/tables/<int:pk>/",TableDetailView.as_view(), name="table-detail"),
]