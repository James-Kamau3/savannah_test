from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer, OrderSerializer
from record.models import Customer
from django.shortcuts import render, redirect
from .forms import AddCustomerForm, AddOrderForm
from django.contrib import messages
from record.utils.africas_talking import send_sms

@api_view(['GET'])
def getData(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


def addOrder(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddOrderForm(request.POST)
            if form.is_valid():

                order = form.save()
                customer = order.customer
                if customer.phone_number:
                    send_sms(recipient=[customer.phone_number], message=f'Hi {customer.name}, your order for {order.item}, has been successfully placed')
                messages.success(request, 'Order added and sms sent')
                return redirect('home')
                    
        else:
            form = AddOrderForm()

    customers = Customer.objects.all()
    return render(request, 'record/add_order.html', {'form': form, 'customers': customers})

def addCustomer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully added')
                return redirect('add_order')

            else:
                messages.error(request, "There was an error with your submission.")
        else:
            form = AddCustomerForm()

    return render(request, 'record/add_customer.html', {'form': form})
            

        
        