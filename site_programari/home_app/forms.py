# forms.py
from django import forms
from .models import Programare

class ProgramareForm(forms.ModelForm):
    class Meta:
        model = Programare
        fields = ['serviciu', 'data', 'ora', 'telefon']  # Include și câmpul pentru telefon
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'ora': forms.TimeInput(attrs={'type': 'time'}),
            'telefon': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Introduceti numărul de telefon'}),
        }
