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
    code = models.PositiveIntegerField(default=generate_unique_code, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

