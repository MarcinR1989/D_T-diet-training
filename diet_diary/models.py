from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class FoodProduct(models.Model):
    name = models.CharField(max_length=128)
    kcal_per_100g = models.FloatField(validators=[MinValueValidator(0)])
    protein_per_100g = models.FloatField(validators=[MinValueValidator(0)])
    carbs_per_100g = models.FloatField(validators=[MinValueValidator(0)])
    fat_per_100g = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=128)
    # Można wpisać ręcznie kcal albo policzyć ze składników(obliczenia w Views)
    dish_kcal = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    food_products = models.ManyToManyField(FoodProduct, through="DishDetails")


class DishDetails(models.Model):
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    food_product_weight = models.FloatField(validators=[MinValueValidator(0)])
