from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LikedRecipe(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    recipeId =  models.ForeignKey('recipes.Recipe', null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    