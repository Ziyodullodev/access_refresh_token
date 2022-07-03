from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshTokenAPIView


urlpatterns = [
    path('reg/', RegisterAPIView.as_view()),
    path('refresh/', RefreshTokenAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', UserAPIView.as_view()),

]
