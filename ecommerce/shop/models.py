from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_ajout']
        
    
    def __str__(self):
        return self.nom
        
        
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField() 
    
    categorie = models.ForeignKey(Categorie, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_ajout = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_ajout']
        
    def __str__(self):
        return self.nom

class Commande(models.Model):
    items = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    ville = models.CharField(max_length=300)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    prenom = models.CharField(max_length=300)
    total = models.CharField(max_length=300)
    
    class Meta:
        ordering = ['-date_commande']
        def __str__(self):
            return self.nom
    
    
    
    
    
    
    
    