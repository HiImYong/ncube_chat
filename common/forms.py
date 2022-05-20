from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fuser #DB의 Fuser와 데이터 비교를 위한 참조
from django.contrib.auth.hashers import check_password #패스워드 비교를 위한 참


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


