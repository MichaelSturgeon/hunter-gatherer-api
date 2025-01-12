# Imported files and packages
from django.urls import path
from reviews import views

# URL patterns for reviews app
urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
]
