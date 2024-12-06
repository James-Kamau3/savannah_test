import logging
from django.shortcuts import render, redirect
from .models import Customer, Order
from django.shortcuts import get_object_or_404
from django.urls import reverse
from authlib.integrations.django_client import OAuth
from django.conf import settings
from urllib.parse import quote_plus, urlencode




# Create your views here.

# oauth = OAuth()

# oauth.register(
#     "auth0",
#     client_id=settings.AUTH0_CLIENT_ID,
#     client_secret=settings.AUTH0_CLIENT_SECRET,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
# )

oauth = OAuth()
oauth.register(
    name='auth0',
    client_id='AUTH0_CLIENT_ID',
    client_secret='AUTH0_CLIENT_SECRET',
    server_metadata_url=f'https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid profile email'
    },
    redirect_uri='http://localhost:3000/callback'
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

    
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("home")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

    
def home(request):
    customers = Customer.objects.all()
    return render(request, 'record/home.html', {'customers': customers})


def orders(request, pk):
    orders = get_object_or_404(Order, id=pk)
    return render(request, 'record/orders.html', {'orders': orders})


