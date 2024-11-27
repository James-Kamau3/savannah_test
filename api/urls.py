from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='view_customers'),
    path('add_customer', views.addCustomer, name='add_customer'),
]
