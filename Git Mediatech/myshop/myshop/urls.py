from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#Cette classe me permets d'inclure toutes les urls de base de mon projet 
#Creer les urls et inclue les différentes url selon leurs packages 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)