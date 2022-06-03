from rest_framework import permissions


class StaffAllButEditOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    # This method only checks if the user is authenticated. If not,
    # the NotAuthenticated exception is raised and access is denied.
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # Granting full access to object's if superuser is accessing them
        if request.user.is_superuser:
            return True

        # Checking if the requested method is one of the SAFE methods
        # like ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
