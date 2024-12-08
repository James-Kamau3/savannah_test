from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from record.models import Customer


#Test fot customer model
class CustomerModelTest(TestCase):

    def test_customer_creation(self):
        customer = Customer.objects.create(
            name="Kasongo",
            phone_number="+254757988864"
        )
        self.assertEqual(customer.name, "Kasongo")
        self.assertEqual(customer.phone_number, "+254757988864")
        self.assertIsInstance(customer, Customer)
