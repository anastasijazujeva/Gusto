from django.urls import path
from . import views # import views from views.py from the same folder

app_name = 'users' # specify app name for later reference

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('view_profile', views.view_profile, name = 'view_profile'),
    path('edit_profile', views.edit_profile, name = 'edit_profile'),
    path('my_ratings', views.rating_list, name = 'rating_list'),
    path('wishlist', views.wishlist_list, name = 'wishlist_list'),
]