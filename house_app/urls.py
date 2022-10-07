from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.Category, name='category'),
    path('add_house/', views.add_house, name='add_house'),

]