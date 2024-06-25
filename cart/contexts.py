from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    grand_total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
