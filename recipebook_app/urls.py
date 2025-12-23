from django.urls import path
from recipebook_app import views
urlpatterns = [
    path("",views.recipe_list, name="recipe-list"),
]