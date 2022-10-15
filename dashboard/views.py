from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import House_Product, Car_Product



def myproducts(request, category_slug=None):

    # if request.user.is_authenticated:
    h_products = House_Product.objects.all().filter(is_available=True,).order_by('id')
    c_products = Car_Product.objects.all().filter(is_available=True,).order_by('id')



    # if category_slug != None:
    #     h_products = House_Product.objects.filter( is_available=True)
    #     c_products = Car_Product.objects.filter( is_available=True)
    #
    #     paginator = Paginator(products, 1)
    #     page = request.GET.get('page')
    #     paged_products = paginator.get_page(page)
    #     product_count = products.count()
    # else:
    #
    #     h_products = House_Product.objects.all().filter(is_available=True).order_by('id')
    #     c_products = Car_Product.objects.all().filter(is_available=True).order_by('id')
    #
    #     paginator = Paginator(h_products, 9)
    #     page = request.GET.get('page')
    #     paged_products = paginator.get_page(page)
    #     product_count = h_products.count()

    context = {
        'h_products' : h_products,
        'c_products': c_products,

        # 'h_products': paged_products,
        # 'product_count': product_count,
    }
    return render(request, 'myproducts.html', context)