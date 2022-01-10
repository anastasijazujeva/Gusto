from django.urls import path
from . import views # import views from views.py from the same folder

app_name = 'products' # specify app name for later reference

urlpatterns = [
    path('', views.product_list, name = 'products'),
    path('<id>/', views.product_details, name = 'product_details'),
    path('<id>/wishlist', views.wishlist, name = 'wishlist'),
]