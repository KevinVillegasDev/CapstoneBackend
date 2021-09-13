from django.db import models

# Create your models here.

class Measurement(models.Model):
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
    
    # TBL - Tablespoon - ALL
    # Gal - Gallon - Liquid
    # Cup - Cup - All
    # cup - Cup - All