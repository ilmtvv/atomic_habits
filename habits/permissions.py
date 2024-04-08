from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in ('HEAD', 'OPTIONS'):
            return True

        return obj.user.pk == request.user.pk
