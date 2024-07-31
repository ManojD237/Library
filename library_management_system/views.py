from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request, 'home.html')

def set_session(request):
    request.session['username'] = 'john_doe'  # Set session data
    request.session.set_expiry(3600)  # Set expiry to 1 hour (3600 seconds)
    return redirect('home')


def get_session(request):
    username = request.session.get('username')  # Retrieve session data
    context = {'username': username}
    return render(request, 'display_session.html', context)

def check_session(request):
    if 'username' in request.session:
        username = request.session['username']
        return render(request, 'display_session.html', {'username': username})
    else:
        return render(request, 'session_expired.html')