from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # Used during url debugging only
from .forms import RecipeForm, RecipeIngredientForm, RecipeIngredientFormSet, RecipeImageForm

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
    
    context = {
        "recipe": recipe.name,
        "ingredients": ingredients,
        "author": author,
        "images": images,
        "pk": num,
    }
    return render(request, "recipe.html", context)

# Renders form for creating a new recipe and/or ingredients as necessary
@login_required
def new_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)

        # Check if both the recipe form and formset are valid
        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            formset.instance = recipe 
            formset.save()  # Save the RecipeIngredient instances

            return redirect('ledger:index')  # Redirect to the index after saving

    else:
        recipe_form = RecipeForm()
        formset = RecipeIngredientFormSet()

    return render(request, 'new_recipe.html', {
        'recipe_form': recipe_form,
        'formset': formset
    })

# Allows adding of an image to a specific recipe page
@login_required
def add_image(request, pk=1):
    recipe = get_object_or_404(Recipe, pk=pk) 
    
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            # Save the image and associate it with the recipe
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect(recipe.get_absolute_url()) 

    else:
        form = RecipeImageForm() 
    
    return render(request, 'new_image.html', {
        'form': form,
        'recipe': recipe
    })