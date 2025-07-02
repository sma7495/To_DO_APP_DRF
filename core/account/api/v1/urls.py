from django.urls import path, include
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegistrationGenericAPIView, CustomTokenObtainPairView

app_name = "api"

urlpatterns = [
    path('registration/',RegistrationGenericAPIView.as_view(), name= "registration"),
    
    # Token Authentication:
    # path('token_login/', ObtainAuthToken.as_view(), name="token_login"),
    
    #JWT Authentication:
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]