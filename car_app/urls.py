from django.urls import path
from . import views

urlpatterns = [
    path('add_car/', views.add_car, name='add_car'),

]