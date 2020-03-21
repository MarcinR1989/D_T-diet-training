from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from diet_diary.forms import AddFoodProductForm, AddDishForm, AddFoodToDishForm
from diet_diary.models import FoodProduct, Dish, DishDetails


# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'base.html')


class FoodProductView(View):
    def get(self, request):
        food_set = FoodProduct.objects.all().order_by('name')
        ctx = {
            "food_set": food_set
        }
        return render(request, 'food_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        FoodProduct.objects.get(id=deleted_data_id).delete()
        return redirect('/food_product_list/')


class AddFoodProductView(View):
    def get(self, request):
        form = AddFoodProductForm()
        AddFoodProductFormSet = formset_factory(AddFoodProductForm, extra=1)
        # formset = AddFoodProductFormSet(initial=[
        #     {'name': 'Jakieś tam jedzonko',
        #      "kcal_per_100g": 100,
        #      "protein_per_100g": 100,
        #      "carbs_per_100g": 100,
        #      "fat_per_100g": 100,
        #      }
        # ])
        ctx = {
            "table_hidden": "hidden",
            "form": form,
            # "formset": formset,
        }
        return render(request, 'food_list_add.html', ctx)

    def post(self, request):
        form = AddFoodProductForm(request.POST)
        if form.is_valid():
            new_added_product = FoodProduct.objects.create(
                name=form.cleaned_data['name'],
                kcal_per_100g=form.cleaned_data['kcal_per_100g'],
                protein_per_100g=form.cleaned_data['protein_per_100g'],
                carbs_per_100g=form.cleaned_data['carbs_per_100g'],
                fat_per_100g=form.cleaned_data['fat_per_100g'],
            )
            ctx = {
                "food_set": [new_added_product],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'food_list_add.html', ctx)


class DishesView(View):
    def get(self, request):
        dish_set = Dish.objects.all().order_by('name')
        ctx = {
            "dish_set": dish_set
        }
        return render(request, 'dishes_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        Dish.objects.get(id=deleted_data_id).delete()
        return redirect('/dishes_list/')


def calculate_kcal(new_object):
    food_kcal_sum = 0
    new_dishdetails = DishDetails.objects.filter(dish=new_object.pk)
    for dish in new_dishdetails:
        weight = dish.food_product_weight
        kcal = dish.food_product.kcal_per_100g
        food_kcal_sum += weight * kcal / 100
    return food_kcal_sum


class AddDishView(View):
    AddFoodToDishFormSet = formset_factory(AddFoodToDishForm, extra=5)

    def get(self, request):
        dish_form = AddDishForm()
        ctx = {
            "table_hidden": "hidden",
            "dish_form": dish_form,
            "dish_food_formset": self.AddFoodToDishFormSet,
        }
        return render(request, 'dish_add.html', ctx)

    def post(self, request):
        dish_form = AddDishForm(request.POST)
        dish_food_formset = self.AddFoodToDishFormSet(request.POST, request.FILES)

        if dish_form.is_valid() and dish_food_formset.is_valid():
            new_added_dish = Dish.objects.create(
                name=dish_form.cleaned_data['dish_name'],
                dish_kcal=dish_form.cleaned_data['dish_kcal'],
            )
            for form in dish_food_formset:
                if form.cleaned_data != {}:
                    DishDetails.objects.create(
                        food_product=form.cleaned_data['food_product'],
                        dish=new_added_dish,
                        food_product_weight=form.cleaned_data['food_product_weight']
                    )

            if not new_added_dish.dish_kcal:
                Dish.objects.filter(pk=new_added_dish.pk).\
                    update(dish_kcal=calculate_kcal(new_added_dish))
            ctx = {
                "dish_set": [new_added_dish],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'dish_add.html', ctx)
            # return HttpResponse('Działa')
        else:
            return HttpResponse(dish_form.errors, dish_food_formset)
