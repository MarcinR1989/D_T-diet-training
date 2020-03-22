from django import forms
from django.forms import SelectDateWidget
from diet_diary.models import FoodProduct, TrainingTypes, Dish, Training


class AddFoodProductForm(forms.Form):
    name = forms.CharField(max_length=128)
    kcal_per_100g = forms.FloatField(min_value=0)
    protein_per_100g = forms.FloatField(min_value=0)
    carbs_per_100g = forms.FloatField(min_value=0)
    fat_per_100g = forms.FloatField(min_value=0)


class AddDishForm(forms.Form):
    dish_name = forms.CharField(label="Dish name", max_length=128)
    # TODO zrobić tak, że jak zostawi się puste pole to policzy kcal autmatycznie. Podpisać to pole dla użytkownika
    # dish_kcal = forms.FloatField(min_value=0, required=False)


class AddFoodToDishForm(forms.Form):
    food_product = forms.ModelChoiceField(queryset=FoodProduct.objects.all())
    food_product_weight = forms.FloatField(min_value=0)


class AddTrainingForm(forms.Form):
    name = forms.CharField(max_length=64)
    type = forms.ModelChoiceField(queryset=TrainingTypes.objects.all())
    duration = forms.IntegerField(min_value=0)
    notes = forms.CharField(max_length=512, required=False)


class AddTrainingTypesForm(forms.Form):
    training_type = forms.CharField(max_length=64)


class DishPlanForm(forms.Form):
    dish = forms.ModelChoiceField(queryset=Dish.objects.all())
    date = forms.DateField(widget=SelectDateWidget)
    time = forms.TimeField()
    notes = forms.CharField(max_length=512, required=False)


class TrainingPlanForm(forms.Form):
    training = forms.ModelChoiceField(queryset=Training.objects.all())
    date = forms.DateField(widget=SelectDateWidget)
    time = forms.TimeField()
    notes = forms.CharField(max_length=512, required=False)


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=120)
    password = forms.CharField(label='password', max_length=120, widget=forms.PasswordInput)
