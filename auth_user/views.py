from rest_framework import viewsets

from auth_user import (models, serializers)

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles all the creation, update and deleting"""
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer