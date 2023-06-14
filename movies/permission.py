from rest_framework import permissions
from rest_framework.views import Request


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method not in permissions.SAFE_METHODS and request.user.is_superuser:
            return True
        return False
