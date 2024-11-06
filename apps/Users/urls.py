from django.urls import path
from .views import (
    register_admin,
    register_farmer,
    register_seller,
    register_whole_seller,
    # activate,
    user_login,
    user_logout,
    user_profile,
    update_password,
    reset_password,
    forgot_password,
    forgot_password_active_url,
    admin_activate,
    pending_user,
)

urlpatterns = [
    path("register/farmer/", register_farmer, name="register_farmer"),
    path("register/whole_seller/", register_whole_seller, name="register_whole_seller"),
    path("register/seller/", register_seller, name="register_seller"),
    path("register/admin/", register_admin, name="register_admin"),
    # path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("admin_activate/<uidb64>/<token>/", admin_activate, name="admin_activate"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="profile"),
    path("update/password/", update_password, name="update_password"),
    path("forgot-password/", forgot_password, name="forgot_password"),
    path(
        "forgot-password/<uid>/<token>",
        forgot_password_active_url,
        name="forgot_password_url",
    ),
    path("reset-password/", reset_password, name="reset_password"),
    path("pendings/",pending_user, name="pendings"),
]
