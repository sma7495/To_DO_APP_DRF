from rest_framework.generics import GenericAPIView
from rest_framework.views import Response, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import RegistrationSerializer, CustomTokenObtainPairSerializer

class RegistrationGenericAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'email': serializer.validated_data["email"],
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    