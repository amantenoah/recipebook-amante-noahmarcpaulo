from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list/', views.index, name="index"), 
    path('recipe/<int:num>', views.recipe, name="recipe"),
]

app_name = "ledger"