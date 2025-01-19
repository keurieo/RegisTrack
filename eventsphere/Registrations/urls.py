"""
URL configuration for the Registrations app.
"""

from django.urls import path
from . import views  # Import views from the same app

APP_NAME = "Registrations"  # Optional: Set an app namespace

urlpatterns = [
    path("login/", views.login_user, name="login"),  # Example route
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout, name="logout"),  # Logout page
   
]
