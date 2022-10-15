from django.urls import path
from . import views

urlpatterns = [
    path('myproducts/', views.myproducts, name='myproducts'),

]