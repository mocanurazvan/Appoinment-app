import os
import django
from datetime import date, time

# Inițializăm Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_programari.settings')
django.setup()

from home_app.models import Programare

# Populăm cu programări fake
programari = [
    Programare(data=date(2024, 1, 15), ora=time(9, 0), serviciu='1D', client='Ion Popescu', telefon='0712345678'),
    Programare(data=date(2024, 1, 15), ora=time(11, 0), serviciu='2D', client='Maria Ionescu', telefon='0712345679'),
    Programare(data=date(2024, 1, 16), ora=time(14, 0), serviciu='3D ', client='Ana Georgescu', telefon='0712345680'),
    Programare(data=date(2024, 1, 17), ora=time(16, 0), serviciu='1D', client='Mihai Vasile', telefon='0712345681'),
    # Adaugă mai multe programări aici
]

# Salvează programările în baza de date
Programare.objects.bulk_create(programari)

print("Programările au fost adăugate cu succes!")
