from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.db.models import Q

from .models import Recipe



class IndexView(generic.ListView):
    template_name = 'plan/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)
        return queryset.order_by('date')
