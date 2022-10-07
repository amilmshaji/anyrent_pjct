from django.urls import path
from . import views

urlpatterns = [
    path('add_furn/', views.add_furn, name='add_furn'),

]