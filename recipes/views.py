from django.shortcuts import render, redirect
from django.http import Http404
from django.views import generic
from django.urls import reverse
from django.db.models import Q
from .forms import RecipeForm, DateForm
from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Recipe.objects.filter( Q(title__icontains=query) |
                Q(course__iexact=query) | Q(tag__icontains=query))
            return queryset.filter(user=self.request.user)
        else:
            return Recipe.objects.filter(user=self.request.user)

class AddRecipeView(generic.CreateView):
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        #It should return an HttpResponse.
        form.instance.user = self.request.user
        return super(AddRecipeView, self).form_valid(form)

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class UpdateRecipeView(generic.UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipes/update_recipe.html'
    success_url = '/recipes/'

class AddToCalendar(generic.UpdateView):
    form_class = DateForm
    model = Recipe
    template_name = 'recipes/add_to_calendar.html'
    success_url = '/recipes/'
