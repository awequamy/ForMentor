
from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('categories/', views.categories),
    path('recipes/', views.RecipeListView.as_view()),

]

