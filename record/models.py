from django.db import models
import random

# Create your models here.

def generate_unique_code():
    while True:
        code = random.randint(1000, 9999)
        if not Customer.objects.filter(code=code).exists():
            return code

class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    code = models.PositiveIntegerField(default=generate_unique_code, unique=True)
    
    def __str__(self):
        return f'name: {self.name} - code: {self.code}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.customer.name} - {self.item}, {self.amount}'
    
    