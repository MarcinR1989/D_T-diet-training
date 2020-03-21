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

from diet_diary.views import MainView, FoodProductView, AddFoodProductView, DishesView, AddDishView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', MainView.as_view(), name="main-site"),
    path('food_product_list/', FoodProductView.as_view(), name="food-product-list"),
    path('add_food_product/', AddFoodProductView.as_view(), name="add-food-product"),
    path('dishes_list/', DishesView.as_view(), name="dishes"),
    path('add_dish/', AddDishView.as_view(), name="add-dish"),

]
