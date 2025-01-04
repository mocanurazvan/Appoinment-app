# models.py
from django.db import models

from django.db import models

class Programare(models.Model):
    date = models.DateField()  # Data programării
    ora = models.TimeField()  # Ora programării
    client = models.CharField(max_length=100, null=True, blank=True)  # Numele clientului (opțional)
    serviciu = models.CharField(max_length=100, default="Serviciu general")  # Tipul serviciului

    def __str__(self):
        return f"{self.date} - {self.ora}"
