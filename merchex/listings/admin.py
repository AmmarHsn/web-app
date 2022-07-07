from django.contrib import admin

# Register your models here.

from listings.models import Band, Listing

# admin.site.register(Band)


class BandAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year', 'band')


admin.site.register(Listing, ListingAdmin)

