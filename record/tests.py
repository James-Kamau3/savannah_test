from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from record.models import Customer, Order


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

# Test for order model
class OrderModelTest(TestCase):
    def test_order_creation(self):
        customer = Customer.objects.create(
            name="Kasongo",
            phone_number="+254757988864"
        )
        order = Order.objects.create(
            customer=customer,
            item="Milo",
            amount=22.76
        )
        self.assertEqual(order.customer.name, "Kasongo")
        self.assertEqual(order.item, "Milo")
        self.assertEqual(order.amount, 22.76)
        self.assertIsInstance(order, Order)