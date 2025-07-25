from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email    = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if both passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        # ✅ Validate password strength
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e:
                messages.error(request, error)
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('home')

    return render(request, 'accounts/signup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get('next', 'home')  # default is 'home'
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')  # Change to your homepage




@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
