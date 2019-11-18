from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete_city/<city_name>', views.delete_city, name='delete_city'),
]
