from django.db import models
from recipes.models import Recipe

#Plan has a many to many relationship with Recipe because many recipes can be
#saved to many plans and many plans can have many recipes. Will show the start
#and end of each plan. Has a one to many relationship with MealPlans
class Plan(models.Model):
    recipes = models.ManyToManyField(Recipe)
    meal_plan = models.ForeignKey('MealPlans', models.SET_NULL, null = True)
    start_date = models.DateField(auto_now = False, auto_now_add = False)
    end_date = models.DateField(auto_now = False, auto_now_add = False)

    

class MealPlans(models.Model):
    pass
