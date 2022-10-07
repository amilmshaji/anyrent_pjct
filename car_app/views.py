from django.shortcuts import render, redirect

# Create your views here.
from .models import Car_Product


def add_car(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        fuel=request.POST.get('fuel')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        car=Car_Product(brand=brand,fuel=fuel,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        car.save()
        return redirect('/')
    return render(request, 'add_car.html')