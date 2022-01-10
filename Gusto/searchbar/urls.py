from django.urls import path
from . import views # import views from views.py from the same folder

app_name = 'searchbar' # specify app name for later reference

urlpatterns = [
    path('', views.search_products, name = 'search_products'),
    path('<id>', views.search_details, name = 'search_details'),
]