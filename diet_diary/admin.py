from django.contrib import admin
from diet_diary.models import FoodProduct#, Dish


# Register your models here.
class FoodProductAdmin(admin.ModelAdmin):
    pass


class DishAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodProduct, FoodProductAdmin)
# admin.site.register(Dish, DishAdmin)
