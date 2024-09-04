from django.contrib import admin
from .models import Categorie, Produit, Commande
# Register your models here.


class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout')
    
class AdminProduit(admin.ModelAdmin):

    list_display = ('nom', 'prix', 'categorie', 'date_ajout')
    search_fields = ('title',)
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'address', 'email', 'ville', 'pays', 'total', 'date_commande')
    


admin.site.register(Produit, AdminProduit)
admin.site.register(Categorie, AdminCategorie)  
admin.site.register(Commande, AdminCommande)

admin.site.index_title = "dev manager" 
admin.site.site_header = "Site E-Commerce"
admin.site.site_title = "BabaShop"