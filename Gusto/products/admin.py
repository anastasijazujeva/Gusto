from django.contrib import admin
from .models import Product, Reviews

# register Product and Reviews tables to admin
admin.site.register(Product)
admin.site.register(Reviews)