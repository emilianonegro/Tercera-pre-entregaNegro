from django.shortcuts import render, redirect
from . import forms

def index(request):
    return render(request, 'home/index.html')

def create_chef(request):
    if request.method == "POST":
        form = forms.ChefForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.ChefForm()
    return render(request, "home/create_chef.html", {"form": form})


def create_recipe(request):
    if request.method == "POST":
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = forms.RecipeForm()
    return render(request, "home/create_recipe.html", {"form": form})
