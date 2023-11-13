from django.contrib import admin
from .models import Product, Employees, Chair

# Register your models here.

admin.site.register(Product)
admin.site.register(Employees)
admin.site.register(Chair)

