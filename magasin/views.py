from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from .forms import ProduitForm, CommandeForm, FournisseurForm ,EditProfileForm
from .models import Produit, Commande, Fournisseur ,Categorie
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
 
from magasin.serializers import CategorySerializer ,ProduitSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView

from rest_framework import viewsets



@login_required
def index(request):
    context={'val':"Menu Acceuil"}
    return render(request,'accueil.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return HttpResponseRedirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'magasin/vitrine.html', {'list': produits})





def prod(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() 
        return render(request,'magasin/majProduits.html',{'form':form}) 
    
def mesProduits(request):
    query = request.GET.get('q')
    produits = Produit.objects.all()
    if query:
        produits = produits.filter(libellé__icontains=query)
    return render(request, 'magasin/vitrine.html', {'list': produits})


def mesprod(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        list=Produit.objects.all()
        return render(request,'magasin/vitrine.html',{'list':list})

def commande(request):
    if request.method == "POST": 
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            commande_instance = form.save(commit=False)
            produits = form.cleaned_data.get('produits')
            total = sum(produit.prix for produit in produits)
            commande_instance.totalCde = total
            commande_instance.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = CommandeForm()
    return render(request, 'magasin/commande.html', {'form': form })

def nouveauFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm() #créer formulaire vide
        list=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'form':form })







class ListeProduits(ListView):
    model = Produit
    template_name = 'magasin/Liste_produit.html'
    context_object_name = 'produits'
class DetailProduit(DetailView):
    model = Produit
    template_name = 'magasin/detail_produit.html'
    context_object_name = 'produit'
class CreerProduit(CreateView):
    model = Produit
    template_name = 'magasin/Créer_produit.html'
    form_class = ProduitForm  
    success_url = reverse_lazy('liste_produits') 
class ModifierProduit(UpdateView):
    model = Produit
    template_name = 'magasin/Modifier_produit.html'
    form_class = ProduitForm  
    success_url = reverse_lazy('magasin:liste_produits')
class SupprimerProduit(DeleteView):
    model = Produit
    template_name = 'magasin/Supprimer_produit.html'
    success_url = reverse_lazy('magasin:liste_produits') 


class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Categorie.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
 
class ProduitAPIView(ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edite_profile.html"
    success_url = reverse_lazy('magasin:liste_produits')  # Redirection vers la page d'accueil de votre application

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        # Enregistrement du formulaire et redirection vers la page d'accueil
        form.save()
        return HttpResponseRedirect(self.get_success_url())

 
# def index(request):
#     if request.method == "POST" : 
#         form = ProduitForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/magasin')
#     else :
#         form = ProduitForm() #créer formulaire vide
#         return render(request,'magasin/majProduits.html',{'form':form})



