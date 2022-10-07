from django.urls import path
from . import views

urlpatterns = [
    path('add_bike/', views.add_bike, name='add_bike'),

]