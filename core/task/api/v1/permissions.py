from rest_framework import permissions


class IsRelatedUserOrManager(permissions.BasePermission):

    def has_permission(self, request, view):

        return True

    def has_object_permission(self, request, view, obj):
        perm = False
        if request.method == "GET":
            perm = True
        elif request.method == "PUT" or request.method == "DELETE":
            if obj.manager.user == request.user:
                perm = True
        return perm
