from django.shortcuts import render
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Renders an index of all available recipes
def index(request):
    recipes = Recipe.objects.all()
    ctx = { 
           "recipes": recipes
        }
    return render(request, "index.html", ctx)

# Shows a specific recipe detailed based on the primary key passed
@login_required
def recipe(request, num=1):
    recipe = Recipe.objects.get(pk=num)
    ingredients = RecipeIngredient.objects.filter(recipe__exact=recipe)
    author = recipe.user
    images = RecipeImage.objects.filter(recipe__exact=recipe)
    
    ctx = {
        "recipe": recipe.name,
        "ingredients": ingredients,
        "author": author,
        "images": images
    }
    return render(request, "recipe.html", ctx)

# Renders form for creating a new recipe and/or ingredients as necessary
@login_required
def new_recipe(request):
    return HttpResponse("hehe")

# Allows adding of images to a specific recipe page
@login_required
def add_image(request, pk=1):
    return "oopsies"