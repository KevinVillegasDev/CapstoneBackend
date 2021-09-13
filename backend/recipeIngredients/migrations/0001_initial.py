# Generated by Django 3.2.7 on 2021-09-13 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
        ('recipes', '0001_initial'),
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=30)),
                ('ingredientId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredient')),
                ('measurement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='measurements.measurement')),
                ('recipeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]