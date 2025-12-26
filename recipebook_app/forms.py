from django import forms
from recipebook_app.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'category', 'ingredients', 'steps']
