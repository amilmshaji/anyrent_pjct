from django.contrib import admin

# Register your models here.
from house_app.models import House_Product

# admin.site.register(Category)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'ad_title',
#         # 'price',
#         # 'stock',
#         # 'category',
#         # 'created_date',
#         # 'modified_date',
#         'is_available',
#         'slug',
#     )
#     prepopulated_fields = {'slug': ('ad_title',)}

admin.site.register(House_Product)

