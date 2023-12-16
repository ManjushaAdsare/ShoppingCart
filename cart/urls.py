from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('myproject.urls')),
    path('', views.List_Products.as_view()),
    path('save-products/', views.AddProductData.as_view()),
    path('view-cart/', views.ViewCart.as_view()),
    path('add/<int:product_id>/', views.AddtoCart.as_view(), name='add_to_cart'),
    path('home', views.Home.as_view(), name='home'),
]
