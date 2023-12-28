from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import datetime  # Import datetime module
from .forms import UserInfoForm  # Import your UserInfoForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import UserInfo
from .forms import UserInfoForm  # Import the UserInfoForm
from django.contrib.auth import login as auth_login, authenticate
from .forms import UserInfoForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        # Process registration form data here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user logic
        user = User.objects.create_user(
            username=username, email=email, password=password)
        if user:
            messages.success(request, 'Registration successful! Please login.')
            # Redirect to the login page after successful registration
            return redirect('/login')
        else:
            messages.error(request, 'Registration failed. Please try again.')

    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = authenticate(
            request, username=username_or_email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/user_info')

        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')


def user_info(request):
    # Set default DOB (January 1, 2000)
    default_dob = datetime(year=2000, month=1, day=1)

    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('ERRORS:_           ', form.errors)
    else:
        # Set initial data for DOB field
        form = UserInfoForm(initial={'dob': default_dob})
    return render(request, 'user_info.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
