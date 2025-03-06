from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True) # to avoid ingredient duplicates
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.id)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.id)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50, null=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_details') # get ingredient from Ingredient
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient') # connect to recipe from Recipe