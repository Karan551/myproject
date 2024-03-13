from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form is submitted successfully.")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})
