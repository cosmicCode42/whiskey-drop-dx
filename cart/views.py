from django.shortcuts import render

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders cart contents """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'cart/cart.html', context)