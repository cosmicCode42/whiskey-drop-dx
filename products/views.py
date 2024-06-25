from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Product

# Create your views here.
def product_detail(request, product_id):
    """ A view to show individual whiskey details """

    products = Product.objects.all()
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)