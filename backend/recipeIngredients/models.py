from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=30)
    recipeId = models.ForeignKey('recipes.Recipe', null=True, blank=True, on_delete=CASCADE)
    ingredientId = models.ForeignKey('ingredients.Ingredient', null=True, blank=True, on_delete=CASCADE)
    measurement = models.ForeignKey('measurements.Measurement', null=True, blank=True, on_delete=CASCADE)
    
    def __str__(self):
        return self.quantity
    
    