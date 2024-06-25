from django.conf import settings

from .models import Product

def products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return context
    