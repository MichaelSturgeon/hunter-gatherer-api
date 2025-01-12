# Imported files and packages
from django.urls import path
from products import views

# URL patterns for products app
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
]
