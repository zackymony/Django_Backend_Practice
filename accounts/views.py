from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')
        else:
            messages.error(request, 'There was a problem creating your account. Please try again.')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': login_form})


