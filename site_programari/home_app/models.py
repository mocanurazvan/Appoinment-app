# models.py
from django.db import models


class Serviciu(models.Model):
    nume = models.CharField(max_length=50)  # Numele serviciului, ex. "Aplicare 1D"
    descriere = models.TextField(blank=True, null=True)  # Descriere opțională
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Prețul serviciului

    def __str__(self):
        return self.nume


class Clienta(models.Model):
    nume = models.CharField(max_length=100)  # Numele cliente
    email = models.EmailField()  # Emailul cliente
    telefon = models.CharField(max_length=15)  # Numărul de telefon

    def __str__(self):
        return self.nume


from django.db import models
from django.utils.timezone import now

class Programare(models.Model):
    clienta = models.ForeignKey('Clienta', on_delete=models.CASCADE)
    serviciu = models.ForeignKey('Serviciu', on_delete=models.CASCADE)
    data = models.DateField()  # Data programării
    ora = models.TimeField()   # Ora programării

    def __str__(self):
        return f"{self.clienta.nume} - {self.serviciu.nume} la {self.data} {self.ora}"

class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Programare {self.client_name} - {self.appointment_date} la {self.appointment_time}"