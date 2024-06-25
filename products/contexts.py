from django.conf import settings

from .models import Product

def products(request):
    """ Allows use of 'products' across the site """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return context
    