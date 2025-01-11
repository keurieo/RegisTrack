"""URL configuration for Events application."""

from django.urls import path, include
from . import views

urlpatterns = [
    # Add your URL patterns here
    # Example: path('', views.home, name='home'),
    path("", views.index, name="index"),
]
