from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible 
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    url = models.URLField(max_length=200, blank=False, default='')
    date = models.DateField(null=True, blank=True)
    tag = models.CharField(max_length = 100, blank=True, null=True)
    ingredients = models.TextField()

    BREAKFAST = 'Breakfast'
    BRUNCH = 'Brunch'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    SIDES = 'Sides'
    SNACKS = 'Snacks'
    DRINKS = 'Drinks'
    COURSE_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (BRUNCH, 'Brunch'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SIDES, 'Sides'),
        (SNACKS, 'Snacks'),
        (DRINKS, 'Drinks'),
        (None, 'None')
    )
    course = models.CharField(
        max_length = 100,
        choices = COURSE_CHOICES,
        null = True,
        default = None,
        blank=True,
    )

    def __str__(self):
        return self.title
