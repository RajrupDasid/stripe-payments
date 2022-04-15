from django.test import TestCase
from .models import Product

class CheckoutTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name='rice', price = 50)
    def test_checkout_model(self):
        t = self.product
        #try:
            #if not price < 200:
        self.assertTrue(isinstance(t,Product))
        self.assertEqual(str(t),'rice')
         #   else:
          #      print('You have some error')
        #except Exception as e:
         #   print('%'*10,e)


