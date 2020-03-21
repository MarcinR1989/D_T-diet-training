from django import forms
from django.forms import CheckboxSelectMultiple

from diet_diary.models import FoodProduct


class AddFoodProductForm(forms.Form):
    name = forms.CharField(max_length=128)
    kcal_per_100g = forms.FloatField(min_value=0)
    protein_per_100g = forms.FloatField(min_value=0)
    carbs_per_100g = forms.FloatField(min_value=0)
    fat_per_100g = forms.FloatField(min_value=0)


class AddDishForm(forms.Form):
    dish_name = forms.CharField(label="Dish name", max_length=128)
    # TODO zrobić tak, że jak zostawi się puste pole to policzy kcal autmatycznie. Podpisać to pole dla użytkownika
    dish_kcal = forms.FloatField(min_value=0, required=False)


class AddFoodToDishForm(forms.Form):
    food_product = forms.ModelChoiceField(queryset=FoodProduct.objects.all())
    food_product_weight = forms.FloatField(min_value=0)
