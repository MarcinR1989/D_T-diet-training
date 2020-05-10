from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from diet_diary.forms import AddFoodProductForm, AddDishForm, AddFoodToDishForm, AddTrainingForm, AddTrainingTypesForm, \
    TrainingPlanForm, DishPlanForm, LoginForm
from diet_diary.models import FoodProduct, Dish, DishDetails, Training, TrainingTypes, DishPlan, TrainingPlan


# Create your views here.
def dish_macronutrient(new_object):
    kcal_sum = 0
    protein_sum = 0
    carbs_sum = 0
    fat_sum = 0
    new_dishdetails = DishDetails.objects.filter(dish=new_object.pk)
    for dish in new_dishdetails:
        weight = dish.food_product_weight
        kcal = dish.food_product.kcal_per_100g
        protein = dish.food_product.protein_per_100g
        carbs = dish.food_product.carbs_per_100g
        fat = dish.food_product.fat_per_100g

        kcal_sum += weight * kcal / 100
        protein_sum += weight * protein / 100
        carbs_sum += weight * carbs / 100
        fat_sum += weight * fat / 100
    return {"kcal": kcal_sum,
            "protein": protein_sum,
            "carbs": carbs_sum,
            "fat": fat_sum}


class MainView(View):
    def get(self, request):
        diet_plan = DishPlan.objects.all().order_by('date', 'time')
        training_plan = TrainingPlan.objects.all().order_by('date', 'time')
        ctx = {
            "diet_plan": diet_plan,
            "training_plan": training_plan,
        }
        return render(request, 'main.html', ctx)


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


class EditFoodProductView(View):
    def get(self, request):
        form = AddFoodProductForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
        }
        return render(request, 'food_list_add.html', ctx)


class AddFoodProductView(View):
    def get(self, request):
        form = AddFoodProductForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
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


# class EditFoodProductView(View):
#     def get(self, request):
#         form = AddFoodProductForm()
#         ctx = {
#             "table_hidden": "hidden",
#             "form": form,
#         }
#         return render(request, 'food_list_add.html', ctx)


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


class AddDishView(View):
    AddFoodToDishFormSet = formset_factory(AddFoodToDishForm, extra=10)

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
                # dish_kcal=dish_form.cleaned_data['dish_kcal'],  # tutaj użytkownik może ręcznie wpisać kcal dish'a
            )
            for form in dish_food_formset:
                if form.cleaned_data != {}:
                    DishDetails.objects.create(
                        food_product=form.cleaned_data['food_product'],
                        dish=new_added_dish,
                        food_product_weight=form.cleaned_data['food_product_weight']
                    )

            if not new_added_dish.dish_kcal:
                Dish.objects.filter(pk=new_added_dish.pk).update(
                    dish_kcal=dish_macronutrient(new_added_dish)["kcal"],
                    dish_protein=dish_macronutrient(new_added_dish)["protein"],
                    dish_carbs=dish_macronutrient(new_added_dish)["carbs"],
                    dish_fat=dish_macronutrient(new_added_dish)["fat"],
                )
            ctx = {
                "dish_set": Dish.objects.filter(pk=new_added_dish.pk),
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'dish_add.html', ctx)
        else:
            return HttpResponse("Something went wrong. Try again.")


class TrainingView(View):
    def get(self, request):
        db_elements = Training.objects.all().order_by('name')
        ctx = {
            "db_elements": db_elements,
        }
        return render(request, 'training_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        Training.objects.get(id=deleted_data_id).delete()
        # update jeszcze trzeba zrobić
        return redirect('/training_list/')


class AddTrainingView(View):
    def get(self, request):
        form = AddTrainingForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
        }
        return render(request, 'training_add.html', ctx)

    def post(self, request):
        form = AddTrainingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_added = Training.objects.create(
                name=form.cleaned_data['name'],
                type=form.cleaned_data['type'],
                duration=form.cleaned_data['duration'],
                notes=form.cleaned_data['notes'],
            )
            ctx = {
                "db_elements": [new_added],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'training_add.html', ctx)


class TrainingTypesView(View):
    def get(self, request):
        db_elements = TrainingTypes.objects.all().order_by('training_type')
        ctx = {
            "db_elements": db_elements,
        }
        return render(request, 'training_types_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        TrainingTypes.objects.get(id=deleted_data_id).delete()
        # update jeszcze trzeba zrobić
        return redirect('/training_types_list/')


class AddTrainingTypesView(View):
    def get(self, request):
        form = AddTrainingTypesForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
        }
        return render(request, 'training_types_add.html', ctx)

    def post(self, request):
        form = AddTrainingTypesForm(request.POST)
        if form.is_valid():
            new_added = TrainingTypes.objects.create(
                training_type=form.cleaned_data['training_type'],
            )
            ctx = {
                "db_elements": [new_added],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'training_types_add.html', ctx)


# NOWE CRUD'y !!! --------------------------------------
class DishPlanView(View):
    def get(self, request):
        db_elements = DishPlan.objects.all().order_by('date', 'time')  # jeszcze raz .order_by('time') ?
        ctx = {
            "db_elements": db_elements,
        }
        return render(request, 'dish_plan_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        DishPlan.objects.get(id=deleted_data_id).delete()
        # update jeszcze trzeba zrobić
        return redirect('/dish_plan_list/')


class AddDishPlanView(View):
    def get(self, request):
        form = DishPlanForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
        }
        return render(request, 'dish_plan_add.html', ctx)

    def post(self, request):
        form = DishPlanForm(request.POST)
        if form.is_valid():
            new_added = DishPlan.objects.create(
                dish=form.cleaned_data['dish'],
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time'],
                notes=form.cleaned_data['notes'],
            )
            ctx = {
                "db_elements": [new_added],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'dish_plan_add.html', ctx)


class TrainingPlanView(View):
    def get(self, request):
        db_elements = TrainingPlan.objects.all().order_by('date', 'time')  # jeszcze raz .order_by('time') ?
        ctx = {
            "db_elements": db_elements,
        }
        return render(request, 'training_plan_list.html', ctx)

    def post(self, request):
        deleted_data_id = request.POST.get("usuń")
        TrainingPlan.objects.get(id=deleted_data_id).delete()
        # update jeszcze trzeba zrobić
        return redirect('/training_plan_list/')


class AddTrainingPlanView(View):
    def get(self, request):
        form = TrainingPlanForm()
        ctx = {
            "table_hidden": "hidden",
            "form": form,
        }
        return render(request, 'training_plan_add.html', ctx)

    def post(self, request):
        form = TrainingPlanForm(request.POST)
        if form.is_valid():
            new_added = TrainingPlan.objects.create(
                training=form.cleaned_data['training'],
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time'],
                notes=form.cleaned_data['notes'],
            )
            ctx = {
                "db_elements": [new_added],
                "hidden": "hidden",
                "method": "POST",
            }
            return render(request, 'training_plan_add.html', ctx)
        else:
            return HttpResponse('Coś poszło nie tak')


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Wrong password or login.')
        else:
            return HttpResponse("There is some kind of error")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')



