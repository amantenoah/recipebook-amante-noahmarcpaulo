from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # Used during url debugging only
from .forms import RecipeForm, IngredientForm, RecipeIngredientFormSet

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
    if request == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)
        ingredient_form = IngredientForm(request.POST)
        
        if recipe_form.is_valid() and formset.is_valid():
            # Handle new ingredient creation if any
            if ingredient_form.is_valid() and ingredient_form.cleaned_data:
                ingredient_form.save()
            
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            
            recipe_ingredient = formset.save(commit=False)
            for form in formset:
                if form.cleaned_data:
                    recipe_ingredient = form.save(commit=False)
                    recipe_ingredient.recipe = recipe
        
            return redirect('ledger:index')
    else:
        recipe_form = RecipeForm()
        new_ingredient_form = IngredientForm()
        formset = RecipeIngredientFormSet()
            
        return render(request, 'new_recipe.html', {
            'recipe_form': recipe_form,
            'ingredient_form': new_ingredient_form,
            'formset': formset
        })

# Allows adding of images to a specific recipe page
@login_required
def add_image(request, pk=1):
    return "oopsies"