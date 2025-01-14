from django.shortcuts import render, redirect
from django.contrib.auth import login  # Import the login function
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to a home page or dashboard
    
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "registration/login.html")
     
    else:
        return render(request, "registration/login.html")


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            auth_login(request, user)
            return redirect("home")  # Redirect to a home page or dashboard
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")  # Redirect to the login page
