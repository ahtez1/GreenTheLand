from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'email',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))


    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))


    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 're-type password',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-3 px-4 rounded-lg'
    }))