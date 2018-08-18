from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
        UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField)



class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }))
    email = forms.EmailField(required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }))
    password1 = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }))

    password2 = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

class EditProfileForm(UserChangeForm):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    email = forms.EmailField(required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))
    password = ReadOnlyPasswordHashField(
        widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',

        )
