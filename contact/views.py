from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from contact import serializers

class ContactInfoViewSet(viewsets.ModelViewSet):
    """Handles contact information CRUD operations"""
    serializer_class = serializers.ContactSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

    def get_queryset(self):
        """Returns the queryset to be used for this"""
        user = self.request.user
        return user.contact_set.all()
    
    def perform_create(self, serializer):
        """Customizations to the process of creating new contacts"""
        serializer.save(author=self.request.user)
