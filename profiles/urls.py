# Imported files and packages
from django.urls import path
from profiles import views

# URL patterns for profiles app
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
