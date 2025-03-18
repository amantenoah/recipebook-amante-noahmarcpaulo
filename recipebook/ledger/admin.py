from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "author"

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient
    extra = 1  

# Added decorators as per django documentation
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )  
    inlines = [RecipeIngredientInline] # Allows full creation of recipe in one tab, including ingredients and quantities

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )  

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'quantity')
    search_fields = ('recipe__name', 'ingredient__name')
    list_filter = ('recipe', 'ingredient')  # Allows filtering by both recipe and ingredient