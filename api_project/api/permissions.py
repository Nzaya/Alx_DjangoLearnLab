from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Write permissions are only allowed to admin users
        return request.user and request.user.is_staff
