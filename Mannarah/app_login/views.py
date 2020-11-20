from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import userSignUpForm
from .models import MyUser, Profile

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def signUpView(request):
    form = userSignUpForm()
    if request.method == 'POST':
        form = userSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request, 'app_login/signup_page.html', {'form': form})


def loginView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_login:home'))
    return render(request, 'app_login/login_page.html', {'form': form})


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))


@login_required
def homeView(request):
    return render(request, 'home.html', {})
