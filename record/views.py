from django.shortcuts import render
from .models import Customer, Order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.

def home(request):
    customers = Customer.objects.all()
    return render(request, 'record/home.html', {'customers': customers})


def orders(request, pk):
    orders = get_object_or_404(Order, id=pk)
    return render(request, 'record/orders.html', {'orders': orders})


