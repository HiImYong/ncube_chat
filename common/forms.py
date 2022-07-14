from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    
    # csrfmiddlewaretoken = forms.CharField()
    email = forms.EmailField(label="email")

    # print(csrfmiddlewaretoken)


    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")



class email_form(forms.Form):
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        fields = ("email")


