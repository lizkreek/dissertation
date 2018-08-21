from django.urls import path
from . import views


app_name='recipes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add-recipe/', views.AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('recipe/<int:pk>/update/', views.UpdateRecipeView.as_view(), name='update'),
    path('add-to-calendar/<int:pk>', views.AddToCalendar.as_view(), name="add_to_calendar"),
]
