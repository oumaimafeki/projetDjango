from django.urls import path ,include
#from django.conf.urls import url
from .views import ListeProduits, DetailProduit, CreerProduit, ModifierProduit, SupprimerProduit,UserEditView
from . import views
from .views import CategoryAPIView, ProduitAPIView,ProductViewset


app_name = 'magasin'



urlpatterns = [
  path('produits/', views.prod, name='prod'),
  path('catalogue/', views.mesProduits, name='catalogue'),
  path('', views.mesprod, name='cat'),
  path('commande/', views.commande, name='commande'),
  path('fournisseur/', views.nouveauFournisseur, name='fournisseur'), # Ajout de la virgule
  path('register/', views.register, name='register'),
  path('logout/',views.logout_view , name="logout"),
  path('<int:pk>/', DetailProduit.as_view(), name='detail_produit'),  
    path('ajouter/', CreerProduit.as_view(), name='creer_produit'),  
    path('<int:pk>/modifier/', ModifierProduit.as_view(), name='modifier_produit'),  
    path('<int:pk>/supprimer/', SupprimerProduit.as_view(), name='supprimer_produit'),
path('liste_produits/', ListeProduits.as_view(), name='liste_produits'),
 path('api-auth/', include('rest_framework.urls')),

  path('api/category/', CategoryAPIView.as_view()),
      path('api/produits/', ProduitAPIView.as_view()),

          path("edit_profile/", UserEditView.as_view(), name="edite_profile"),
          




]
