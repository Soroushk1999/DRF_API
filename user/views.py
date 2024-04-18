from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth.models import User

from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Check if user is authenticated
        if self.request.user.is_authenticated:
            return UserProfile.objects.filter(user=self.request.user)
        else:
            return UserProfile.objects.none()

    def perform_create(self, serializer):
        # Check if user is authenticated
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            return Response({"error": "User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(ObtainAuthToken):
    serializer_class = UserSerializer
