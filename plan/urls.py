from django.urls import path
from django.conf.urls import include, url
from . import views
from django.views.generic import View

app_name = 'plan'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

]
