"""Auth URL Configuration """
from rest_framework_simplejwt.views import TokenObtainPairView

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("me/", views.UserAPIView.as_view(), name="me"),
]
