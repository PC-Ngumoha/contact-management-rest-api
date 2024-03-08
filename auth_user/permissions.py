from rest_framework import permissions


class UpdateOwnAccount(permissions.BasePermission):
    """User can only update their own account"""

    def has_object_permission(self, request, view, obj):
        """Determine user permissions"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
