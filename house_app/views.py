from django.shortcuts import render, redirect

# Create your views here.
from house_app.models import House_Product


def Category(request):

    return render(request, 'category.html')

def add_house(request):
    if request.method=="POST":
        type=request.POST.get('type')
        furnish=request.POST.get('furnish')
        bedroom=request.POST.get('bedroom')
        bathroom=request.POST.get('bathroom')

        builtup = request.POST.get('builtup')
        capacity = request.POST.get('capacity')
        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        house=House_Product(type=type,furnish=furnish,bedroom=bedroom,bathroom=bathroom,
                            builtup=builtup,capacity=capacity,rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        house.save()
        return redirect('/')
    return render(request, 'add_house.html')