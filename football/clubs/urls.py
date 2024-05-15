# clubs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modifier_club/<int:id>/', views.modifier_club, name='modifier_club'),
    path('supprimer_club/<int:id>/', views.supprimer_club, name='supprimer_club'),
    path('modifier_joueur/<int:id>/', views.modifier_joueur, name='modifier_joueur'),
    path('supprimer_joueur/<int:id>/', views.supprimer_joueur, name='supprimer_joueur'),
]
