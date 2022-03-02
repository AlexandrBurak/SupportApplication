from rest_framework.permissions import SAFE_METHODS, BasePermission

from tickets.models import Support


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsSupporter(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'PATCH']:
            return Support.objects.filter(supporter=request.user).exists()
        return False
