from django import forms
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage
from django.forms import inlineformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
        
# https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/#inline-formsets
RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields = ['ingredient', 'quantity'],
    extra=1,
)