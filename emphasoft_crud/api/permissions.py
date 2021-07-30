from rest_framework import permissions


#Ограничение доступа к чужим записям

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user