from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=30)
    measurement = models.ForeignKey('measurements.Measurement', null=True, blank=True, on_delete=CASCADE)
    
    def __str__(self):
        return self.name