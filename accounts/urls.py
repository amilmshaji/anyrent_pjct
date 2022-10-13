from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),

]
