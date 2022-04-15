from django.test import TestCase
from .models import Product


class CheckoutTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='rice', price=50)

    def test_checkout_model(self):
        t = self.product
        self.assertTrue(isinstance(t, Product))
        self.assertEqual(str(t), 'rice')
