from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getData, name='home'),
    path('add_customer', views.addCustomer, name='add_customer'),
    path('add_order', views.addOrder, name='add_order')
]
