from django.shortcuts import render
from recipebook_app import Recipe
# Create your views here.

def recipe_list(request): 
    recipes = Recipe.objects.all()
    return render(
        request,
        "recipe_list.html",
        {"recipes": recipes}
    )
