from django.shortcuts import render
from .models import Customer, Order
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    customers = Customer.objects.all()
    return render(request, 'record/home.html', {'customers': customers})


    
