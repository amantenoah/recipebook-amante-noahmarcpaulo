from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.index, name="index"), 
    path('recipe/<int:num>', views.recipe, name="recipe"),
    path('recipe/add', views.new_recipe, name="add_recipe"),
    path('recipe/<int:pk>/add_image', views.add_image, name="add_image")
]

app_name = "ledger"