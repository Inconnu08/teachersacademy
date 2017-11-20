from rest_auth.views import LoginView

from .models import User
from .serializers import UserPublicSerializer, RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework import generics, permissions


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    # no need as default rest settings set to this already
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = UserPublicSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    lookup_field = 'id'


class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer


class Login(LoginView):
    serializer_class = LoginSerializer


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
