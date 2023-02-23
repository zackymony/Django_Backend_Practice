from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeacherRegistrationForm, StudentRegistrationForm

def register(request):
    if request.method == 'POST':
        if request.POST.get('role') == 'teacher':
            form = TeacherRegistrationForm(request.POST)
        else:
            form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('account/login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        if request.GET.get('role') == 'teacher':
            form = TeacherRegistrationForm()
        else:
            form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'accounts/login_success.html')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': login_form})


