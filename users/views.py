from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout, login

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/users/login/")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("This is form.get_user()", form.get_user())
            login(request, form.get_user())
            return redirect("post:post_list")
            # return HttpResponse("Form is submitted.")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("/")
