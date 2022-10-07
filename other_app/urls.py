from django.urls import path
from . import views

urlpatterns = [
    path('add_other/', views.add_other, name='add_other'),

]