
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from magasin.views import CategoryAPIView, ProduitAPIView,ProductViewset

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('jeu/', include('jeu.urls')),
path('api/', include(router.urls)),

    path('',views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')) ,
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
