from django.db import models

# Create your models here.
class Feature(models.Model):

	icon = models.CharField(max_length=254)
	name = models.CharField(max_length=254)
	description = models.TextField()
	is_new = models.BooleanField(default=False)


class Quote(models.Model):
    
    image = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    quote = models.CharField(max_length=254)
    

class Favourite(models.Model):
    
    rank = models.DecimalField(max_digits=3, decimal_places=0)
    name = models.CharField(max_length=254)
    country_of_origin = models.CharField(max_length=254)