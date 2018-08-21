import datetime
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import generic
from django.urls import reverse
from recipes.models import Recipe
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=6)
        return Recipe.objects.filter(date__range=(start_date, end_date))
