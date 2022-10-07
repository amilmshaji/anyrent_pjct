from django.contrib import admin
from .models import Account

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude =('password',)

admin.site.register(Account,UserAdmin)
