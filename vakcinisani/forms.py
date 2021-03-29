from django.forms import ModelForm
from .models import Vakcinisan
from django import forms
from django.core.exceptions import ValidationError


class VakcinisanForm(ModelForm):
    class Meta:
        model = Vakcinisan
        fields = [
            'ime',
            'prezime',
            'jmbg',
            'vakcina',
            'alergija',
            'email_1',
            'email_2',
        ]
        widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control'}),
            'prezime': forms.TextInput(attrs={'class':'form-control'}),
            'jmbg': forms.TextInput(attrs={'class': 'form-control'}),
            'email_1': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}),
            'email_2': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}),
            'vakcina': forms.Select(attrs={'class': 'form-control'}),
            'alergija': forms.CheckboxInput()
        }

    def clean_jmbg(self):
        data = self.cleaned_data['jmbg']
        for char in data:
            if not char.isdigit():
                raise forms.ValidationError("Neispravan JMBG. Maticni broj se sastoji samo od cifara!")
            return data

    def clean(self):
            cleaned_data = super().clean()
            email_1 = cleaned_data.get("email_1")
            email_2 = cleaned_data.get("email_2")

            if email_1 and email_2:
                # Only do something if both fields are valid so far.
                if email_1 != email_2:
                    print("nisu iste adrese")
                    raise forms.ValidationError(
                        "Email adrese nisu iste"
                    )
