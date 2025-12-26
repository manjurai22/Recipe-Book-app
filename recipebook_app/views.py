from django.shortcuts import render,redirect
from recipebook_app.models import Recipe
from recipebook_app.forms import RecipeForm
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
            return redirect("recipe_list") 
    else:
        form = RecipeForm()  # Empty form for GET request

    return render(request, "add_recipe.html", {"form": form})

def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id) 
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "edit_recipe.html", {"form": form,"recipe":recipe})

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)  
    recipe.delete()  
    return redirect("recipe_list")

def search_recipe(request):
    query = request.GET.get('q')

    recipes = []
    if query:
        recipes = Recipe.objects.filter(
            name__icontains=query
        ) | Recipe.objects.filter(
            category__icontains=query
        )

    return render(request, 'search_recipe.html', {
        'recipes': recipes,
        'query': query
    })