from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='products/Product/')
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Employees(models.Model):
    image = models.ImageField(upload_to='products/staff/')
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Chair(models.Model):
    image = models.ImageField(upload_to='products/Products')
    title = models.CharField(max_length=60)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title