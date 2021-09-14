from django.urls import path
from recipeIngredients import views


urlpatterns = [
    path('recipeingredients', views.RecipeIngredientList.as_view()),
    path('recipeingredients/<int:pk>/', views.RecipeIngredientDetail.as_view())
]