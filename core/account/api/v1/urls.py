from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken

from .views import RegistrationGenericAPIView

app_name = "api"

urlpatterns = [
    path('registration/',RegistrationGenericAPIView.as_view(), name= "registration"),
    path('token_login/', ObtainAuthToken.as_view(), name="token_login"),
]