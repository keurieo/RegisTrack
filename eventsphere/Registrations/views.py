from django.shortcuts import render, redirect
from django.contrib.auth import login  # Import the login function
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Events.urls import urlpatterns

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("")  # Render the correct template
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "registration/login.html")  # Re-render login page with error
    return render(request, "registration/login.html")  # Render login form for GET request


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            auth_login(request, user)
            return render(request, 'Registrations/login/base.html')  # ✅ Correct, renders the template

        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def logout(request):
    # Log the user out
    auth_logout(request)
    # Show a success message
    messages.success(request, "You have been logged out.")
    # Redirect to the login page
    return redirect("home")

def home(request):
    return render(request, 'base.html')