from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('orders/<int:pk>', views.orders, name='orders'),
    # path('orders', views.orders, name='orders'),
]
