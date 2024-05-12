from django.forms import ModelForm
from .models import Produit
from .models import Commande
from .models import Fournisseur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.forms import UserChangeForm



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" 
    
class CommandeForm(ModelForm):
    class Meta : 
        model = Commande 
        fields = "__all__" 

class FournisseurForm(ModelForm):
    class Meta : 
        model = Fournisseur 
        fields = "__all__" 
