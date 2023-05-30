from django import forms
from . import models

class ChefForm(forms.ModelForm):
 class Meta:
  model = models.Chef
  fields = '__all__'
  
class RecipeForm(forms.ModelForm):
 class Meta:
  model = models.Recipe
  fields = '__all__'