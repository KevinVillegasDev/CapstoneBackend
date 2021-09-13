from rest_framework import serializers
from .models import RecipeIngredient

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'quantity', 'recipeId', 'ingredientId', 'measurement']