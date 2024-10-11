from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Quote, Favourite, Feature

# Create your views here.

def index(request):
    """ A view to return the index page """
    quotes = Quote.objects.all()
    favourites = Favourite.objects.all()
    features = Feature.objects.all()

    context = {
        'quotes': quotes,
        'favourites': favourites,
        'features': features,
    }

    return render(request, 'home/index.html', context)