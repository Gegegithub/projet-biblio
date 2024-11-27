from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import utilisateur
from django.contrib.auth import logout
from .models import Livre
from django.utils import timezone  # Ajoute cette ligne pour timezone
from datetime import timedelta  # Ajoute cette ligne pour timedelta
from .models import Emprunt
from django.contrib.auth.decorators import login_required

# Vue d'inscription
def inscription(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')  # Récupération du nom d'utilisateur
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        promo = request.POST.get('promo')

        if password == confirm_password:
            # Créer l'utilisateur avec create_user pour gérer correctement le mot de passe
            user = utilisateur.objects.create_user(
                username=username,  # Nom d'utilisateur
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,  # Django gère le hash du mot de passe automatiquement
                promo=promo,
                role='student',  # Rôle par défaut
            )
            user.save()
            return redirect('auth_app:connexion')  # Redirige vers la page de connexion après l'inscription
        else:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})

    return render(request, 'inscription.html')

# Vue de connexion
def connexion(request):
    if request.method == 'POST':
        # Récupère le nom d'utilisateur ou l'email et le mot de passe
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Recherche de l'utilisateur
        user = None
        if '@' in username_or_email:
            # Si c'est un email, on cherche par email
            user = utilisateur.objects.filter(email=username_or_email).first()
        else:
            # Sinon, on cherche par nom d'utilisateur
            user = utilisateur.objects.filter(username=username_or_email).first()

        # Si l'utilisateur est trouvé et que le mot de passe est correct
        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('auth_app:accueil')  # Redirige vers la page d'accueil après la connexion
        else:
            # Message d'erreur si les informations de connexion sont incorrectes
            return render(request, 'connexion.html', {'error': 'Identifiants invalides.'})

    return render(request, 'connexion.html')



# Vue pour la déconnexion
def deconnexion(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('auth_app:connexion')  # Redirige vers la page de connexion


# Vue pour la page d'accueil
def index(request):
    return render(request, 'accueil.html')

def livre(request , livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    return render(request, 'livre.html'  , {'livre': livre})


def liste_livre(request):
    livres = Livre.objects.all()  # Récupérer tous les livres
    return render(request, 'accueil.html', {'livres': livres})

def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)  # Récupère le livre à emprunter
    
    if request.method == 'POST':  # Vérifie si la méthode est POST
        # Calcul des dates
        date_emprunt = timezone.now()  # Date actuelle
        date_retour = date_emprunt + timedelta(weeks=2)  # Date de retour après 2 semaines
        
        # Créer et sauvegarder l'emprunt
        emprunt = Emprunt.objects.create(
            utilisateur=request.user,  # Utilisateur actuellement authentifié
            livre = livre,  # Livre que l'utilisateur emprunte
            date_emprunt=date_emprunt,  # Date d'emprunt actuelle
            date_retour=date_retour  # Date de retour calculée
        )

        # Réduire le nombre d'exemplaires disponibles du livre
        livre.nombre_exemplaires -= 1
        livre.save()

 # Si ce n'est pas une requête POST, redirige vers la liste des livres
    return redirect('auth_app:accueil')    
