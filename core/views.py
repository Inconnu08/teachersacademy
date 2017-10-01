from rest_auth.views import LoginView

from .models import User
from .serializers import UserPublicSerializer, RegistrationSerializer, LoginSerializer
from rest_framework import generics, permissions


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserPublicSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    lookup_field = 'id'


class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer


class Login(LoginView):
    serializer_class = LoginSerializer