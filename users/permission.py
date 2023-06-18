from rest_framework import permissions
from rest_framework.views import Request


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        user_id = view.kwargs.get("user_id")
        user = request.user
        """
        if se o usuario nao possue token
        
        if se é empregado e 
        se é o mesmo id ou admin
        """
        if not request.auth:
            return False
        if user.id == user_id or request.user.is_employee:
            return True
        return False

