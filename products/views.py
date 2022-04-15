from django.views import View
from stripe import *
from django.conf import settings


stripe.api_key=settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self,request,*args,**kwargs):
        checkout_session=stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data':{
                            'currency' : 'usd',
                            'unit_amount' : 2000,
                            'product_data' :{
                                    'name': 'Stubborn Attachments',
                                    'images': ['https://www.aquariumofpacific.org/images/news/Japanese_Sea_Nettle14_FLAT.jpg']
                                },
                            },
                            'quantity':1,
                    },
                    ],
                    mode='payment'
                    success_url=YOUR_DOMAIN + '/success.html',
                    cancel_url=YOUR_DOMAIN + '/cancel.html'
                )

