from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/<int:pk>', views.orders, name='orders'),
]
