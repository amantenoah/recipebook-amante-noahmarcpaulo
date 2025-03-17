from django.shortcuts import render
from .models import Recipe, RecipeIngredient, Ingredient
# Create your views here.

def index(request):
    # Just gets all recipes since everything needed can be accessed from there
    recipes = Recipe.objects.all()
    ctx = { 
           "recipes": recipes
        }
    return render(request, "index.html", ctx)

def recipe(request, num=1):
    recipe = Recipe.objects.get(pk=num)
    ingredients = RecipeIngredient.objects.filter(recipe__exact=recipe)
    ctx = {
        "recipe": recipe.name,
        "ingredients": ingredients
    }
    return render(request, "recipe.html", ctx)