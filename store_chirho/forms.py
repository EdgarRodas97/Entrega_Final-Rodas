from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm


class RegisterUserFormChirho(UserCreationForm):
    email_chirho = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña:", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre:")
    last_name = forms.CharField(label="Apellido:")

    class Meta:
        model = User
        fields=["email_chirho", "username", "first_name", "last_name", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña:", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modificar Nombre:")
    last_name = forms.CharField(label="Modificar Apellido:")

    class Meta:
        model = User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}
        

class CreateOfferFormChirho(ModelForm):
        class Meta:
            model = PostChirho
            fields = [
                'title_chirho',
                'post_type_chirho',
                'post_chirho',
                'contact_chirho',
                'price_chirho',
                'post_picture_chirho',
            ]

