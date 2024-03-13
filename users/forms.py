from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Enter Your Name:",
        max_length=255,
        widget=forms.TextInput({"placeholder": "Enter Your Name:"}),
    )
    email = forms.EmailField(label="Enter Your Email:", max_length=255)
    password1 = forms.CharField(
        label="Password :",
        widget=forms.PasswordInput(
            {"placeholder": "Enter Your Password :", "autocomplete": "username"}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password :",
        widget=forms.PasswordInput(
            {
                "placeholder": "Enter Your Confirm Password :",
                "autocomplete": "new-pasword",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email")

    # name.widget.attrs.update({"placeholder": "Enter Your Name :"})
    email.widget.attrs.update({"placeholder": "Enter Your Email :"})
