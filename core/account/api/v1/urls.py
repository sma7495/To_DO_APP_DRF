from django.urls import path, include
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegistrationGenericAPIView, CustomTokenObtainPairView, VerifyUserToken, UserChangePassword

app_name = "api"

urlpatterns = [
    path('registration/',RegistrationGenericAPIView.as_view(), name= "registration"),
    path('change_password/',UserChangePassword.as_view(), name="change_password"),
    
    # Token Authentication:
    # path('token_login/', ObtainAuthToken.as_view(), name="token_login"),
    
    #JWT Authentication:
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/<str:token>/', VerifyUserToken.as_view(), name="verify"),
]