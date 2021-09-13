from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    instructions = models.TextField(max_length=3000)
    category = models.ForeignKey('categories.Category', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    