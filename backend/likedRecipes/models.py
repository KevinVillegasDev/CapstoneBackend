from django.db import models

# Create your models here.

class LikedRecipe(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE)
    recipeId =  models.ForeignKey('recipes.Recipe', null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    