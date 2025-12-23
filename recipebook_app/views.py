from django.shortcuts import render,redirect
from recipebook_app.models import Recipe

# Create your views here.

def recipe_list(request): 
    recipes = Recipe.objects.all()
    return render(
        request,
        "recipe_list.html",
        {"recipes": recipes}
    )

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")  # Redirect to the recipe list page after adding
    else:
        form = RecipeForm()  # Empty form for GET request

    return render(request, "add_recipe.html", {"form": form})


