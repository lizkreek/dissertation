from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    url = models.URLField(max_length=200, blank=False, default='')
    cal_date = models.DateField(null=True)
    tag = models.CharField(max_length = 100, null = True)
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
    )

    def __str__(self):
        return self.title
