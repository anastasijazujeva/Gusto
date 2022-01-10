from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('home', include('main.urls')),
    path('products/', include('products.urls')),
    path('account/', include('users.urls')),
    path('search_products/', include('searchbar.urls')),
]

# connect static files and media to make a design for the app and upload images
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)