from django.shortcuts import render
# from .models import Category
from django.shortcuts import get_object_or_404, redirect, render
from house_app. models import House_Product
# from cart.models import CartItem, Cart
# from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, InvalidPage
from django.db.models import Q
# Create your views here.
def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        products = House_Product.objects.filter( is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:

        products = House_Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'shop.html', context)

# def allProdCat(request,c_slug=None):
#     c_page=None
#     products_list=None
#     if c_slug!=None:
#
#         c_page=get_object_or_404(Category,slug=c_slug)
#         products_list=Product.objects.all().filter(category=c_page,available=True)
#     else:
#         products_list=Product.objects.all().filter(available=True)
#     paginator=Paginator(products_list,6)
#     try:
#         page=int(request.GET.get('page','1'))
#     except:
#         page=1
#     try:
#         products=paginator.page(page)
#     except (EmptyPage,InvalidPage):
#         products=paginator.page(paginator.num_pages)
#     return render(request,"shop.html",{'category':c_page,'products':products})