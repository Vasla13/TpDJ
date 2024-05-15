from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Joueur
from .forms import ClubForm, JoueurForm

def index(request):
    club_form = ClubForm()
    joueur_form = JoueurForm()

    if request.method == 'POST':
        if 'ajouter_club' in request.POST:
            club_form = ClubForm(request.POST)
            if club_form.is_valid():
                club_form.save()
                return redirect('index')
        elif 'ajouter_joueur' in request.POST:
            joueur_form = JoueurForm(request.POST)
            if joueur_form.is_valid():
                joueur_form.save()
                return redirect('index')

    clubs = Club.objects.all()
    joueurs = Joueur.objects.all()

    return render(request, 'clubs/index.html', {
        'club_form': club_form,
        'joueur_form': joueur_form,
        'clubs': clubs,
        'joueurs': joueurs
    })

def modifier_club(request, id):
    club = get_object_or_404(Club, id=id)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClubForm(instance=club)
    return render(request, 'clubs/modifier_club.html', {'form': form})

def supprimer_club(request, id):
    club = get_object_or_404(Club, id=id)
    if request.method == 'POST':
        club.delete()
        return redirect('index')
    return render(request, 'clubs/supprimer_club.html', {'club': club})

def modifier_joueur(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JoueurForm(instance=joueur)
    return render(request, 'clubs/modifier_joueur.html', {'form': form})

def supprimer_joueur(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    if request.method == 'POST':
        joueur.delete()
        return redirect('index')
    return render(request, 'clubs/supprimer_joueur.html', {'joueur': joueur})