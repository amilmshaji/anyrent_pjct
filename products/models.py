from django.db import models
from django.urls.base import reverse
from django.db.models.signals import pre_save

from accounts.models import Account
from anyrent_pjct.utils import unique_slug_generator


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name  #shows the name


#house product table
class House_Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    ad_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True)
    rent = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    builtup= models.IntegerField()
    capacity= models.IntegerField()
    type = models.CharField(max_length=200,blank=True)
    furnish = models.CharField(max_length=200,blank=True)
    images = models.ImageField(upload_to='photos/house')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)


    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=House_Product)





class Car_Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    ad_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True)
    rent = models.IntegerField()
    brand = models.CharField(max_length=200,blank=True)
    driven = models.IntegerField()
    own = models.CharField(max_length=200,blank=True)
    fuel = models.CharField(max_length=200,blank=True)
    images = models.ImageField(upload_to='photos/house')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=2)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Car_Product)


class Bike_Product(models.Model):
    ad_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True)
    rent = models.IntegerField()
    brand = models.CharField(max_length=200,blank=True)
    driven = models.IntegerField()
    own = models.CharField(max_length=200,blank=True)
    images = models.ImageField(upload_to='photos/house')


    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=3)

    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Bike_Product)


class Furn_Product(models.Model):                #Furniture table product adding table
    ad_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True)
    rent = models.IntegerField()
    images = models.ImageField(upload_to='photos/house')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    type = models.CharField(max_length=200,blank=True)


    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=4)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

def slug_generator(sender,instance,*args,**kwargs):   #To make slug in the table when vendor add products
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Furn_Product)



class Other_Product(models.Model):                #Other table product adding table
    ad_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,editable=False)
    add_info = models.TextField(max_length=500, blank=True)
    rent = models.IntegerField()
    images = models.ImageField(upload_to='photos/house')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    type = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=5)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.ad_title

def slug_generator(sender,instance,*args,**kwargs):   #To make slug in the table when vendor add products
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Other_Product)


class All_Products(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    house = models.ForeignKey(House_Product, on_delete=models.CASCADE)
    # variations = models.ManyToManyField(Variation, blank=True)
    car = models.ForeignKey(Car_Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    proudct_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # def sub_total(self):
    #     return self.product.price*self.quantity
    #
    # def __unicode__(self):
    #     return self.product





