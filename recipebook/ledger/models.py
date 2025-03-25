from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True) # to avoid ingredient duplicates
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.id)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True) # Had to add a default value for the already existing data
    updated_on = models.DateTimeField(auto_now=True)
    
    # Added a foreignKey to connect it to a user
    # Made the foreignKey accept NULL and Blank so that django would not have a seizure when I made the migrations
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_recipe')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.id)])

class RecipeImage(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_image")
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50, null=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_details') # get ingredient from Ingredient
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient') # connect to recipe from Recipe