from django.urls import path
from . import views # import views from views.py from the same folder

app_name = 'main' # specify app name for later reference

urlpatterns = [
    path('', views.main, name = 'main'),
    path('home', views.home, name = 'home'),
]