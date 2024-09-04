from django.shortcuts import render, redirect
from .models import Produit, Commande
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    produit_objet = Produit.objects.all()
    item_name = request.GET.get("item-name")
    if item_name != "" and item_name is not None:
        produit_objet = Produit.objects.filter(nom__icontains=item_name)
        
    # implementation de la pagination
    paginator = Paginator(produit_objet, 4)
    page = request.GET.get('page')
    produit_objet = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'produit_objet':produit_objet})

def detail(request, myId):
    produit_objet = Produit.objects.get(id = myId)
    return render(request, 'shop/detail.html', {'produit':produit_objet})
    
def validerAchat(request):
    if request.method == "POST":
        items = request.POST.get('items')
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        address = request.POST.get('address')
        email = request.POST.get('email')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        total = request.POST.get('total')
        commande = Commande(items=items, total=total ,nom=nom, prenom=prenom, address=address,  email=email, ville=ville, pays=pays, zipcode=zipcode)
        commande.save()
        return redirect('confirmation')
        
    return render(request, "shop/validerAchat.html")  

def confirmation(request):
    commande = Commande.objects.all()[:1]
    for item in commande:
        nom = item.nom
    
    return render(request, 'shop/confirmation.html', {'nom':nom})

