from django.shortcuts import render, redirect
from . import forms, models

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

    # Obtener el parámetro de búsqueda desde la solicitud POST o GET
    search_query = request.GET.get('search_query')

    # Realizar la consulta a la base de datos si hay un parámetro de búsqueda
    if search_query:
        recipes = models.Recipe.objects.filter(title__icontains=search_query)
    else:
        recipes = models.Recipe.objects.all()

    return render(request, "home/create_recipe.html", {"form": form, "recipes": recipes})