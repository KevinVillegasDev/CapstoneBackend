from rest_framework import serializers
from .models import LikedRecipe

class LikedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedRecipe
        fields = ['id', 'user', 'recipeId']