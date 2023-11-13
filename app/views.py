from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from.models import Employees
from .models import Chair

# Create your views here.

def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {"product":product, "navbar":"home"})

def about(request):
    staff = Employees.objects.all()
    return render(request, 'about.html', {"staff":staff, "navbar":"about"})

def blog(request):
    return render(request, 'blog.html', {"navbar":"blog"})

def cart(request):
    return render(request, 'cart.html', {"navbar":"cart"})

def checkout(request):
    return render(request, 'checkout.html', {"navbar":"checkout"})

def services(request):
    product = Product.objects.all()
    return render(request, 'services.html', {"product":product ,"navbar":"services"})

def shop(request):
    chair = Chair.objects.all()
    return render(request, 'shop.html', {"chair":chair, "navbar":"shop"})

def thankyou(request):
    return render(request, 'thankyou.html', {"navbar":"thankyou"})

def contact(request):
    return render(request, 'contact.html', {"navbar":"contact"})


