from django.urls import path
from . import views  # Import views from the same app

app_name = 'Registrations'  # Optional: Set an app namespace

urlpatterns = [
    path('', views.index, name='index'),  # Example route
    # Add other paths here
]
