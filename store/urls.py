from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.storeview),
    path('/cart_add_items',views.add_cart_items),
    path('/cart',views.cartview),
    path('/search-item',views.searching),
    path('/search-item-view',views.searchview),
]