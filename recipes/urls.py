from django.urls import path
from . import views


app_name='recipes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipe/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add-recipe/', views.AddRecipeView.as_view(), name='add_recipe'),

]
