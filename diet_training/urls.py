"""diet_training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from diet_diary.views import MainView, FoodProductView, AddFoodProductView, DishesView, AddDishView, ContactView, \
    TrainingView, AddTrainingView, AddTrainingTypesView, TrainingTypesView, DishPlanView, AddDishPlanView, \
    TrainingPlanView, AddTrainingPlanView, EditFoodProductView, LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', MainView.as_view(), name="main-site"),
    path('food_product_list/', FoodProductView.as_view(), name="food-product-list"),
    path('food_product_list_edit/', EditFoodProductView.as_view(), name="food-product-list-edit"),
    path('add_food_product/', AddFoodProductView.as_view(), name="food-product-add"),
    path('dishes_list/', DishesView.as_view(), name="dish-list"),
    path('add_dish/', AddDishView.as_view(), name="dish-add"),

    path('training_list/', TrainingView.as_view(), name="training-list"),
    path('training_add/', AddTrainingView.as_view(), name="training-add"),
    path('training_types_list/', TrainingTypesView.as_view(), name="training-types-list"),
    path('training_types_add/', AddTrainingTypesView.as_view(), name="training-types-add"),
    path('dish_plan_list/', DishPlanView.as_view(), name="dish-plan-list"),
    path('dish_plan_add/', AddDishPlanView.as_view(), name="dish-plan-add"),
    path('training_plan_list/', TrainingPlanView.as_view(), name="training-plan-list"),
    path('training_plan_add/', AddTrainingPlanView.as_view(), name="training-plan-add"),

    path('contact/', ContactView.as_view(), name="contact-me"),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

]
