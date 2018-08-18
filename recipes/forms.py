from django import forms
from django.forms import ModelForm
from .models import Recipe



class RecipeForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class':'form-control',
        }
    ))
    ingredients = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
    }
    ))
    tag = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    COURSE_CHOICES = (
        (None, 'none'),
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Sides', 'Sides'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
    )
    course = forms.CharField(label="Course",
        widget=forms.Select(choices=COURSE_CHOICES,
        attrs={
            'class':'form-control',
        }))


    class Meta:
        model = Recipe
        fields = ['title', 'url', 'tag', 'ingredients', 'course']
