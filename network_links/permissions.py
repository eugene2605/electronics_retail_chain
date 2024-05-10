from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    message = "Вы не являетесь активным пользователем"

    def has_permission(self, request, view):
        print(request.user.is_active)
        return request.user.is_active
