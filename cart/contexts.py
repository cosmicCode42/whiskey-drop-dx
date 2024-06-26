from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product

def cart_contents(request):
    """ allows use of 'cart_contents' across the site"""

    cart_items = []
    grand_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        grand_total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
