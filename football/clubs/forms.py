from django import forms
from .models import Club, Joueur

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nom', 'ville', 'date_fondation']

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'position', 'club']