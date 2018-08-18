from django.urls import path

from . import views

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import reverse_lazy


app_name='home'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name = 'login'),

    path('logout/', LogoutView.as_view(), {'template_name': 'registration/logout.html'}, name='logout'),

    path('register/', views.register, name = 'register'),

    path('profile/', views.view_profile, name = 'view_profile'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('password_change/', views.change_password, name='change_password'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        success_url=reverse_lazy('home:password_reset_done'),
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('home:password_reset_complete')),
        name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete')
]
