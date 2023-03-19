from django import forms
from .models import Usuario

class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class':'forml'}))
    password = forms.CharField(label="Password", max_length="64", widget=forms.PasswordInput(attrs={'class':'forml'}))

class Registro(forms.Form):
    username = forms.CharField(label="Username", max_length="128", widget=forms.TextInput(attrs={'class':'forml'}))
    email = forms.CharField(label="email", max_length="256", widget=forms.TextInput(attrs={'class':'forml'}))
    password = forms.CharField(label="Password", max_length="64", widget=forms.PasswordInput(attrs={'class':'forml'}))

