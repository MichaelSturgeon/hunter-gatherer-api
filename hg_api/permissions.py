# Imported files and packages
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Checks to see if a user is the owner of an object.
    If not renders the object as read only and removes forms
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
