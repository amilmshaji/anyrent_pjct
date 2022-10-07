from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from django.urls.conf import include
from django.conf import settings

admin.site.unregister(Group)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('accounts.urls')),
    path('', include('house_app.urls')),
    path('', include('car_app.urls')),
    path('', include('shop_app.urls')),
    path('', include('bike_app.urls')),
    path('', include('funiture_app.urls')),
    path('', include('other_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
