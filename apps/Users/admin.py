from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "updated_at",
    )  # Columns to show in the list view
    list_filter = (
        "is_staff",
        "is_active",
    )  # Enable filtering by is_staff and is_active
    search_fields = ("name", "email")  # Enable searching by name and email
    ordering = ("-date_joined",)  # Default ordering of the list view
    fields = (
        "name",
        "email",
        "image",
        "address",
        "phone",
        "is_staff",
        "is_active",
        "date_joined",
        "updated_at",
    )  # Fields to display in the edit form
    readonly_fields = (
        "date_joined",
        "updated_at",
    )  # Making the date_joined and updated_at fields read-only
