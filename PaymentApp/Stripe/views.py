import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, TemplateView
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class CancelView(TemplateView):
    template_name = 'cancel.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class ItemView(DetailView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        my_domain = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        },
                    },
                    'adjustable_quantity': {'enabled': True, 'minimum': 1, 'maximum': 5},
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url=my_domain + '/success',
            cancel_url=my_domain + '/cancel',
        )

        return JsonResponse({
            'id': checkout_session.id
        })
