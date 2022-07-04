from django.urls import path
from .views import IjaraAPIView, createuser, IjaraUpdateAPIView


urlpatterns = [
    path('ijara/', IjaraAPIView.as_view()),
    path('ijara/<int:pk>/', IjaraUpdateAPIView.as_view()),
    path('create/', createuser)
]