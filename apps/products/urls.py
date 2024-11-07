# products/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path("list/", views.product_list, name="product_list"),
    path("search/", views.product_search, name="product_search"),
]
