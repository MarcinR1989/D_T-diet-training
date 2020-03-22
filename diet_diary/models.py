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
    name = models.CharField(max_length=128, unique=True)
    dish_kcal = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    dish_protein = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    dish_carbs = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    dish_fat = models.FloatField(validators=[MinValueValidator(0)], blank=True, null=True)
    food_products = models.ManyToManyField(FoodProduct, through="DishDetails")

    def __str__(self):
        return self.name


class DishDetails(models.Model):
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    food_product_weight = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.dish.name + ": " + self.food_product.name


class DishPlan(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.dish.name + ", " + str(self.date)


class TrainingTypes(models.Model):
    training_type = models.CharField(max_length=64)

    def __str__(self):
        return self.training_type


class Training(models.Model):
    name = models.CharField(max_length=64)
    type = models.ForeignKey(TrainingTypes, on_delete=models.CASCADE)
    duration = models.IntegerField(validators=[MinValueValidator(0)])
    notes = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name


class TrainingPlan(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.training.name + ": " + str(self.date)
