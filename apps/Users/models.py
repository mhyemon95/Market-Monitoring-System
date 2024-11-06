from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    Group,
)
from django.core.mail import send_mail
from django.utils import timezone
from django_resized import ResizedImageField
import uuid


# Custom manager for User model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role="Normal-User"):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        # Automatically assign the user to the correct group based on their role
        role_to_group_map = {
            "admin": "ADMIN",
            "farmer": "FARMER",
            "whole_seller": "WHOLESELLER",
            "seller": "SELLER", 
        }

        # Assign group based on role if it exists
        group_name = role_to_group_map.get(role.lower(), "SELLER")
        group, _ = Group.objects.get_or_create(name=group_name)
        group.user_set.add(user)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password, role="admin")
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True, unique=True)
    image = ResizedImageField(upload_to="profile/", default="profile/default.jpg")
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)  # Admin or staff flag
    is_active = models.BooleanField(default=True)  # Active user flag
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
