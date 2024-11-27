from django.urls import path
from . views import*
from . import views



app_name = 'auth_app' #cette ligne permet de chercher les liens dans l'app

urlpatterns = [
    path('inscription/', inscription, name='inscription'),  #
    path('connexion/', connexion, name='connexion'),        
    path('accueil/', liste_livre, name='accueil'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    
    path('livre/<int:livre_id>/', views.livre, name='livre'),  # Détail d'un livre
    path('livre/<int:livre_id>/emprunter/', views.emprunter_livre , name='emprunter_livre'),

]

