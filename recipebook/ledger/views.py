from django.shortcuts import render
from .models import Recipe, RecipeIngredient, User
from django.contrib.auth.decorators import login_required

def index(request):
    # Just gets all recipes since everything needed can be accessed from there
    recipes = Recipe.objects.all()
    ctx = { 
           "recipes": recipes
        }
    return render(request, "index.html", ctx)

@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(pk=num)
    ingredients = RecipeIngredient.objects.filter(recipe__exact=recipe)
    author = recipe.user
    
    ctx = {
        "recipe": recipe.name,
        "ingredients": ingredients,
        "author": author
    }
    return render(request, "recipe.html", ctx)