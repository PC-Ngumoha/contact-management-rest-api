from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import  api_settings

from auth_user import models
from auth_user import serializers
from auth_user import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles all the creation, update and deleting"""
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnAccount,)
    serializer_class = serializers.UserSerializer


class UserLoginView(ObtainAuthToken):
    """Handles user login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES