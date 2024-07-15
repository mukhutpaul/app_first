from django.db import models

# Create your models here.

class Categorie(models.Model):
    codcat = models.CharField(max_length=10,primary_key=True)
    libcat = models.CharField(max_length=30)
    
    def __str__(self):
        name = self.libcat
        return name
    
class Produit(models.Model):
    codeprod = models.CharField(max_length=10,primary_key=True)
    libprod = models.CharField(max_length=30)
    pu = models.IntegerField()
    qte =models.IntegerField()
    
    codcat = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    
    def __str__(self):
        name = self.libprod
        return name


