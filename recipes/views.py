from django.shortcuts import render, redirect
from django.http import Http404
from django.views import generic
from django.urls import reverse
from django.db.models import Q
from .forms import RecipeForm
from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all()

class AddRecipeView(generic.CreateView):
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = '/recipes/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        #It should return an HttpResponse.
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class UpdateRecipeView(generic.UpdateView):
    form_class =RecipeForm
    model = Recipe
    template_name = 'recipes/update_recipe.html'
    success_url = '/recipes/'

def searchRecipes(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = (Q(title__icontains=query) |
                Q(course__iexact=query) | Q(tag__icontains=query))
            results = Recipe.objects.filter(lookups).distinct()
            context={'results': results, 'submitbutton': submitbutton}
            return render(request, 'recipes/search.html', context)

        else:
            return render(request, 'recipes/search.html')

    else:
        return render(request, 'recipes/search.html')


#class SearchView(generic.ListView):
#    paginate_by = 20

#    def get_template_names(self):
#        return ['recipes/search.html']

#    def get_queryset(self):
#        query = self.request.GET.get('q')
#        recipes = Recipe.objects.all()
#        if query:
#            recipes=recipes.filter(
#                Q(title__icontains=query) |
#                Q(tag__icontains=query) |
#                Q(course__icontains=query)
#            )
#        return recipes
