# clubs/models.py

from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    date_fondation = models.DateField()

    def __str__(self):
        return self.nom

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='joueurs')

    def __str__(self):
        return self.nom
