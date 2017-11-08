from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Custom permssion to only allow owner of resource to edit it.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class UserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj # is the request from the user itself?
