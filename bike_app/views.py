from django.shortcuts import render, redirect

# Create your views here.
from .models import  Bike_Product


def add_bike(request):
    if request.method=="POST":
        brand=request.POST.get('brand')
        # year=request.POST.get('year')
        driven=request.POST.get('driven')
        own=request.POST.get('own')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        bike=Bike_Product(brand=brand,driven=driven,own=own,
                            rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        bike.save()
        return redirect('/')
    return render(request, 'add_bike.html')