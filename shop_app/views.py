from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Car_Product, House_Product, Bike_Product, Furn_Product, Other_Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, InvalidPage
from django.db.models import Q
# Create your views here.


def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        h_products = House_Product.objects.filter( is_available=True)
        c_products = Car_Product.objects.filter( is_available=True)
        b_products = Bike_Product.objects.filter( is_available=True)
        f_products = Furn_Product.objects.filter( is_available=True)
        o_products = Other_Product.objects.filter( is_available=True)





        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:

        h_products = House_Product.objects.all().filter(is_available=True).order_by('id')
        c_products = Car_Product.objects.all().filter(is_available=True).order_by('id')
        b_products = Bike_Product.objects.all().filter(is_available=True).order_by('id')
        f_products = Furn_Product.objects.all().filter(is_available=True).order_by('id')
        o_products = Other_Product.objects.all().filter(is_available=True).order_by('id')


        paginator = Paginator(h_products, 9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = h_products.count()

    context = {
        'h_products' : h_products,
        'c_products': c_products,
        'b_products': b_products,
        'f_products': f_products,
        'o_products': o_products,
        # 'h_products': paged_products,
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

#
# def my_products(request, total=0, quantity=0, cart_item=None, cart_items=None):
#     try:
#         tax = 0
#         grand_total = 0
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.filter(
#                 user=request.user, is_active=True)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#
#         for cart_item in cart_items:
#             total += (cart_item.product.price*cart_item.quantity)
#             quantity += cart_item.quantity
#         tax = (2*total)/100
#         grand_total = total+tax
#     except ObjectDoesNotExist:
#         pass
#
#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax': tax,
#         'grand_total': grand_total
#     }
#
#     return render(request, 'cart.html', context)