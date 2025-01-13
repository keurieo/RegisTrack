from django.shortcuts import render

def login(request):
    return render(request, 'registration/login.html')

def registration(request):
    return render(request, 'registration/register.html')