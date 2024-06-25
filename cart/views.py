from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that renders cart contents """

    context = {}
    
    return render(request, 'cart/cart.html', context)