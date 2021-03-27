from django.forms import ModelForm
from .models import Vakcinisan
from django import forms


class VakcinisanForm(ModelForm):
    class Meta:
        model = Vakcinisan
        fields = [
            'ime',
            'prezime',
            'jmbg',
            'vakcina',
            'alergija',
        ]
    def clean_jmbg(self):
        data = self.cleaned_data['jmbg']
        for char in data:
            if not char.isdigit():
                raise forms.ValidationError("Neispravan JMBG. Maticni broj se sastoji samo od cifara!")
            return data
