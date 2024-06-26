from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from cart.contexts import cart_contents

# Create your views here.
def checkout(request):
    """ A view to return the checkout page """
    cart = request.session.get('cart', {})
    if not cart:
        return redirect(reverse('index'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    
    return render(request, template, context)