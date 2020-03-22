from django.contrib import admin
from diet_diary.models import FoodProduct, Dish, DishPlan, DishDetails, Training, TrainingTypes, TrainingPlan


# Register your models here.
@admin.register(FoodProduct)
class FoodProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass
    # filter_horizontal = ('food_products', )


@admin.register(DishDetails)
class DishDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(DishPlan)
class DishPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingTypes)
class TrainingTypesAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    pass
