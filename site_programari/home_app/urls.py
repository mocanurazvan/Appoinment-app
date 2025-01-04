from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),  # Aceasta va fi pagina principală
    path('about/', views.about, name='about'),
    path('cursuri/', views.cursuri, name='cursuri'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('disponibilitate/', views.disponibilitate, name='disponibilitate'),
    path('AlegeServiciu/', views.AlegeServiciu, name='AlegeServiciu'),
    path('formular-clienta/', views.formular_clienta, name='formular_clienta'),
    path('confirma-serviciul/', views.confirma_serviciul, name='confirma_serviciul'),
    path('finalizare-programare/', views.finalizare_programare, name='finalizare_programare'),
    path('confirma-programare/', views.confirma_programare, name='confirma_programare'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
