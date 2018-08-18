from django.shortcuts import render, redirect
from django.http import Http404
from django.views import generic
from django.urls import reverse
from .forms import RecipeForm
from .models import Recipe
from itertools import chain




class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        pass

class AddRecipeView(generic.TemplateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    def get(self, request):
        form = RecipeForm()
        args = {'form': form,
                }
        return render(request, self.template_name, args)

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        #import pdb; pdb.set_trace()
        context = super().get_context_data(**kwargs)

        return context


#class RecipeView(generic.DetailView):
#    model = Recipe
#    template_name = 'recipes/add_recipe.html'



#    def post(self, request):
#        form = RecipeForm(request.POST)
#        if form.is_valid():
#            recipe = form.save(commit=False)
#            recipe.user = request.user
#            recipe.save()
#            text = form.cleaned_data['title', 'photo', 'description', 'prep_time', 'cook_time',
#                'servings', 'yields', 'directions']
#            form = RecipeForm()
#            return redirect('recipes:index')

#        args = {'form': form, 'text': text}
#        return render(request, self.template_name, args)
