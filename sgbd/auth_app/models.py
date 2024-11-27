from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    promo = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Ajout d'un nom unique
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Ajout d'un nom unique
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100, blank=True)  # Auteur facultatif
    resume = models.TextField()
    nombre_exemplaires = models.PositiveIntegerField(default=1)  # Nombre d'exemplaires disponibles
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Chemin vers l'image

    def __str__(self):
        return self.titre
    


class Emprunt(models.Model):
    utilisateur = models.ForeignKey(utilisateur, on_delete=models.CASCADE)  # Relation avec le modèle utilisateur
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)  # Relation avec le modèle Livre
    date_emprunt = models.DateField()  # Date d'emprunt
    date_retour = models.DateField(null=True, blank=True)  # Date de retour (peut être vide si pas encore retourné)

    def __str__(self):
        return f"{self.utilisateur.username} a emprunté {self.livre.titre} le {self.date_emprunt}"

    class Meta:
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"
