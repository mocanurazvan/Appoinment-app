# forms.py
from django import forms
from .models import Clienta

class ClientaForm(forms.ModelForm):
    class Meta:
        model = Clienta
        fields = ['nume', 'email', 'telefon']
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numele complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numărul de telefon'}),
        }

from django import forms
from django.utils.timezone import now

class DataProgramareForm(forms.Form):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Selectează data"
    )
