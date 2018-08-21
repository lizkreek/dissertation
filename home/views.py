from django.shortcuts import render, redirect, reverse
from home.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy


def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('home:view_profile'))
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'home/register.html', args)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'home/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home:view_profile'))

    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'home/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('home:view_profile'))
        else:
            return redirect(reverse('home:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'home/change_password.html', args)
