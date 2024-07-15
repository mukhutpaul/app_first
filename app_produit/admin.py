from django.contrib import admin
from app_produit.models import Categorie,Produit

# Register your models here.

admin.site.register(Categorie,list_display=('codcat','libcat'),search_fields=['libcat'])

admin.site.register(Produit,list_display=('codeprod','libprod','pu','qte','codcat'),search_fields=['libprod'],list_filter=['codcat'])


