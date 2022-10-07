from django.shortcuts import render, redirect

# Create your views here.
from .models import Other_Product


def add_other(request):
    if request.method=="POST":
        type = request.POST.get('type')

        rent = request.POST.get('rent')
        ad_title = request.POST.get('ad_title')
        add_info = request.POST.get('add_info')
        images=request.FILES['images']
        car=Other_Product(type=type,rent=rent,ad_title=ad_title,add_info=add_info,images=images)
        car.save()
        return redirect('/')
    return render(request, 'add_other.html')