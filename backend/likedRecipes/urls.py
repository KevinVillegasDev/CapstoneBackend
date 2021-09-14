from django.urls import path
from likedRecipes import views


urlpatterns = [
    path('likedrecipes', views.LikedRecipeList.as_view()),
    path('likedrecipes/<int:pk>/', views.LikedRecipeDetail.as_view())
    
]