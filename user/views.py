from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model, login

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer, LoginSerializer

User = get_user_model()


@extend_schema(
    parameters=[
        OpenApiParameter('id', description='A unique product ID', type=int),
    ],
    responses={
        200: OpenApiResponse(description='Product details', response=UserProfileSerializer),
        404: OpenApiResponse(description='Product not found'),
    }
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
