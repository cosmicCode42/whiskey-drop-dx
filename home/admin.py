from django.contrib import admin
from .models import Feature, Quote, Favourite

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'icon',
        'name',
        'description',
        'is_new',
    )


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'quote',
    )


class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        'rank',
        'name',
        'country_of_origin',
    )

    ordering = ('rank',)


admin.site.register(Feature, FeatureAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Favourite, FavouriteAdmin)