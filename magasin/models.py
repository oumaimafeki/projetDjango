from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
 (0,"Draft"),
 (1,"Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image=models.ImageField(blank=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title


class Categorie (models.Model):
    TYPE_CHOICES=[
        ('Al','Alimentaire'),
        ('Mb','Meuble'),
        ('Sn','Sanitaire'),
        ('Vs','Vaisselle'),
        ('Vt','Vêtement'),
        ('Jx','Jouets'),
        ('Lg','Linge de Maison'),
        ('Bj','Bijoux'),
        ('Dc','Décor')
        ]
    name=models.CharField(max_length=50,default='Alimentaire',choices=TYPE_CHOICES)
    def __str__(self) :
        return 'name : '+self.name
class Fournisseur (models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return 'nom : '+self.nom+', adresse: '+self.adresse+', email: '+self.email+', telephone: '+self.telephone
class Produit (models.Model):
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    categorie=models.ForeignKey(Categorie ,on_delete=models.CASCADE,null=True) 
    Fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return 'Libellé: ' + self.libellé + ', Description: ' + self.description + ', Prix: ' + str(self.prix) + ', Type: ' + self.type +', categorie: '+str(self.categorie)
class ProduitNC(Produit):
    duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return "Durée garantie: " + self.duree_garantie + " " + super().__str__()
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    produits = models.ManyToManyField(Produit)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)

    def calculer_total(self):
        total = sum(produit.prix for produit in self.produits.all())
        return total

    def save(self, *args, **kwargs):
        self.totalCde = self.calculer_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande du {self.dateCde}, total = {self.totalCde}"
    


    


