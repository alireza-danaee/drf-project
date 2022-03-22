from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')





class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        
        return bool(
            obj.author == request.user or
            request.user and
            request.user.is_superuser
        )


class IsSuperUserOrIsStaffReadOnly(BasePermission):

    def has_permission(self , request , view):

        


        return bool(
            request.user and request.user.is_staff and request.method in SAFE_METHODS or
            request.user and request.user.is_superuser
        )

        
        
        
        
        
        
        
        
        