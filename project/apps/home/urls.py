from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-chef/", views.create_chef, name="create-chef"),
    path("create-recipe/", views.create_recipe, name="create-recipe"),
]
