from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),  # Aceasta va fi pagina principală
    path('about/', views.about, name='about'),
    path('cursuri/', views.cursuri, name='cursuri'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('disponibilitate/', views.disponibilitate, name='disponibilitate'),

]
