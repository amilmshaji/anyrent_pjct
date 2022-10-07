from django.db import models

from django.db.models.signals import pre_save

from anyrent_pjct.utils import unique_slug_generator
from shop_app.models import Category


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
    category = models.CharField(max_length=200,default="Bike")


    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
