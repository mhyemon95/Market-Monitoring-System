from .models import User
from django.core.exceptions import PermissionDenied


def is_admin(user):
    if isinstance(user, User):
        return user.groups.filter(name="admin").exists()  # Changed from "ADMIN" to "admin"
    return False

def is_farmer(user):
    if isinstance(user, User):
        return user.groups.filter(name="farmer").exists()  # Changed from "F" to "farmer"
    return False

def is_wholesaler(user):
    if isinstance(user, User):
        return user.groups.filter(name="wholesaler").exists()  # Changed from "wholesaler"
    return False

def is_seller(user):
    if isinstance(user, User):
        return user.groups.filter(name="normal").exists()  # Changed from "STUDENT" to "normal"
    return False

def user_is_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not is_admin(user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def user_is_farmer(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not is_farmer(user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def user_is_wholesaler(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not is_wholesaler(user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def user_is_seller(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not is_seller(user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view
