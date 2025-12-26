from django.urls import path
from recipebook_app import views
urlpatterns = [
    path("",views.recipe_list, name="recipe_list"),
    path("add-recipe/", views.add_recipe, name="add_recipe"),
    path("edit-recipe/<int:id>",views.edit_recipe,name="edit_recipe"),
    path('delete-recipe/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path("search/", views.search_recipe, name="search_recipe"), 
]