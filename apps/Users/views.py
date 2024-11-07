from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone
from .tokens import generate_tokens
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from MMS import settings
from django.http import HttpResponse
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str


# Register a new student (public sign-up)
def register_farmer(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register_farmer")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("register_farmer")

        # Create a new student user
        new_user = User.objects.create_user(
            email=email, password=password, role="farmer"
        )
        new_user.is_active = False
        new_user.save()

        messages.success(
            request,
            "Your account has been successfully created. Please check your email to activate your account.",
        )

        current_site = get_current_site(request)
        email_subject = "Confirm your email"
        email_body = render_to_string(
            "users/email_confirmation.html",
            {
                "name": name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": generate_tokens.make_token(new_user),
                "link": reverse(
                    "activate",
                    kwargs={
                        "uidb64": urlsafe_base64_encode(force_bytes(new_user.pk)),
                        "token": generate_tokens.make_token(new_user),
                    },
                ),
            },
        )

        email = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [new_user.email],
        )
        email.fail_silently = True
        email.send()

        return redirect("login")

    return render(request, "users/register_farmer.html")

def register_seller(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register_seller")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("register_seller")

        # Create a new student user
        new_user = User.objects.create_user(
            email=email, password=password, role="seller"
        )

        new_user.is_active = False
        new_user.phone = phone
        new_user.address = address
        # new_user.name = name
        new_user.save()

        messages.success(
            request,
            "Your account has been successfully created. Please check your email to activate your account.",
        )

        current_site = get_current_site(request)
        email_subject = "Confirm your email"
        email_body = render_to_string(
            "users/email_confirmation.html",
            {
                "name": name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": generate_tokens.make_token(new_user),
                "link": reverse(
                    "admin_activate",
                    kwargs={
                        "uidb64": urlsafe_base64_encode(force_bytes(new_user.pk)),
                        "token": generate_tokens.make_token(new_user),
                    },
                ),
            },
        )

        email = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [new_user.email],
        )
        email.fail_silently = True
        email.send()

    return render(request, "users/register_seller.html")

def register_whole_seller(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register_whole_seller")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("register_whole_seller")

        new_user = User.objects.create_user(
            email=email, password=password, role="whole_seller"
        )
        new_user.is_active = False
        new_user.save()

        messages.success(
            request,
            "Your account has been successfully created. Please check your email to activate your account.",
        )

        current_site = get_current_site(request)
        email_subject = "Confirm your email"
        email_body = render_to_string(
            "users/email_confirmation.html",
            {
                "name": name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(new_user.pk)),
                "token": generate_tokens.make_token(new_user),
                "link": request.build_absolute_uri(reverse(
                    "admin_activate",
                    kwargs={
                        "uidb64": urlsafe_base64_encode(force_bytes(new_user.pk)),
                        "token": generate_tokens.make_token(new_user),
                    },
                ),)
            },
        )

        email = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [new_user.email],
        )
        email.fail_silently = True
        email.send()

        return redirect("login")

    return render(request, "users/register_whole_seller.html")


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         newuser = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         newuser = None

#     if newuser is not None and generate_tokens.check_token(newuser, token):
#         newuser.is_active = True
#         newuser.save()
#         messages.success(request, "Account activated successfully!")
#         login(request, newuser)
#         return redirect("profile")  # Ensure 'user_profile' exists in your urls.py
#     else:
#         return render(request, "users/activation_failed.html")

def admin_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        newuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        newuser = None

    if newuser is not None and generate_tokens.check_token(newuser, token):
        newuser.is_active = False
        if request.method == "POST":
            newuser.business_name = request.POST.get("business_name", "")
            newuser.business_registration_number = request.POST.get("business_registration_number", "")
            newuser.gst_number = request.POST.get("gst_number", "")
            newuser.wholesale_license_number = request.POST.get("wholesale_license_number", "")

        newuser.save()

        messages.success(request, "Account activated successfully!")
        return render(request,'users/pending.html')  # Ensure 'user_profile' exists in your urls.py
    else:
        return render(request, "users/activation_failed.html")

def pending_user(request):
    if request.user.is_staff:
        pending_users = User.objects.filter(is_active=False)
        return render(request,'users/pending_user.html', {'pending_users':pending_users})
    else:
        return redirect('profile')
    


def forgot_password(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            forgot_user = User.objects.filter(email=email).exists()
            if forgot_user:
                forgot_user_object = User.objects.get(email=email)
                current_site = get_current_site(request)
                email_subject = "Forgot Password"
                email_body = render_to_string(
                    "users/email_forgot_password.html",
                    {
                        "name": forgot_user_object.name,
                        "domain": current_site.domain,
                        "uid": forgot_user_object.pk,
                        "token": generate_tokens.make_token(forgot_user_object),
                    },
                )
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [forgot_user_object.email],
                )
                email.fail_silently = True
                email.send()
            messages.success(request, "Email sent successfully")
            return redirect("login")
        return render(request, "users/forgot_password.html")
    else:
        return redirect("forgot_password")


def forgot_password_active_url(request, uid, token):
    try:
        resetuser = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        resetuser = None

    if resetuser is not None and generate_tokens.check_token(resetuser, token):
        return render(request, "users/reset_password.html", {"uid": uid})
    else:
        return render(request, "users/activation_failed.html")


def reset_password(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        password1 = request.POST["psw"]
        password2 = request.POST["psw-repeat"]

        try:
            resetuser = User.objects.get(pk=uid)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            resetuser = None
        if resetuser is not None:
            if password1 != password2:
                messages.error(request, "Password didn't match!")
                return render(request, "users/reset_password.html", {"uid": uid})
            resetuser.set_password(password1)
            resetuser.save()
            messages.success(request, "Your password has been successfully updated")
    return redirect("login")



# Register an admin (only superuser can create)
@login_required
def register_admin(request):
    if not request.user.is_superuser:
        messages.error(request, "Only superusers can create admin accounts.")
        return redirect("admin_dashboard")

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register_admin")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("register_admin")

        # Create a new admin user
        user = User.objects.create_user(email=email, password=password, role="admin")
        user.name = name
        user.save()

        messages.success(request, "Admin account created successfully!")
        return redirect("profile")

    return render(request, "users/register_admin.html")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = User.objects.get(email=email)
                print(user.email)
            except User.DoesNotExist:
                messages.error(request, "Unknown email. Please contact administration.")
                return redirect("login")

            if user.check_password(password):
                _logout_previous_sessions(user)
                login(request, user)
                user = request.user
                return redirect("profile")

            else:
                messages.error(request, "Incorrect password!")
                return redirect("login")
        return render(request, "users/login.html")


def user_logout(request):
    if request.user.is_authenticated:
        user = request.user
        _logout_previous_sessions(user)
        auth_logout(request)
        messages.success(request, "You have been logged out successfully.")
    return redirect("login")


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    return render(request, "users/profile.html", {"user": user})


def update_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            current_password = request.POST["current_psw"]
            password1 = request.POST["psw"]
            password2 = request.POST["psw-repeat"]

            # Check if the current password is correct
            user = authenticate(email=request.user.email, password=current_password)
            if user is None:
                messages.error(request, "Current password is incorrect")
                return render(request, "users/update_password.html")

            try:
                resetuser = request.user

            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                resetuser = None
            if resetuser is not None:
                if password1 != password2:
                    messages.error(request, "Password didn't match!")
                    return render(request, "users/update_password.html")
                resetuser.set_password(password1)
                resetuser.save()
                login(request, resetuser)
                messages.success(request, "Your password has been successfully updated")
                return redirect("profile")
            else:
                messages.error(request, "User not authenticated!")
                print("User not authenticated!")

        return render(request, "users/update_password.html")



# def _logout_previous_sessions(user):
#     # Filter all sessions where _auth_user_id matches the user id
#     Session.objects.filter(
#         expire_date__gte=timezone.now(),
#         session__contains=user.id
#     ).delete()


def _logout_previous_sessions(user):
    # Get all sessions
    all_sessions = Session.objects.filter(expire_date__gte=timezone.now())

    # Loop through all active sessions
    for session in all_sessions:
        session_data = session.get_decoded()
        # If the session belongs to the same user, delete it
        if session_data.get("_auth_user_id") == str(user.id):
            session.delete()


# class User(AbstractUser):
#     session_key = models.CharField(max_length=40, blank=True, null=True)


# def user_login(request):
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Store the session key for the user
#         user.session_key = request.session.session_key
#         user.save()

#         # Redirect or return response


# from django.contrib.sessions.models import Session

# def _logout_previous_sessions(user):
#     if user.session_key:
#         # Find and delete the session using the stored session key
#         Session.objects.filter(session_key=user.session_key).delete()
