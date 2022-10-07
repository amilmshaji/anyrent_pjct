from django.contrib import admin

# Register your models here.
from funiture_app.models import Furn_Product, Category

admin.site.register(Furn_Product)
admin.site.register(Category)

