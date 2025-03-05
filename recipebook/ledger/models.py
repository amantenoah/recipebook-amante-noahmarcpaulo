from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50, null=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_details')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient')