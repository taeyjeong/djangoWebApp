from django.urls import path
from . import views

# URL Configuration model
urlpatterns = [
    path('homer/', views.say_hi),
    path('marge/', views.say_hello)
]