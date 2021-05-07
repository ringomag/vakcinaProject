from django.forms import ModelForm
from .models import Vakcinisan, Bolest
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime


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
            'bolest_id',
        ]
        widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control'}),
            'prezime': forms.TextInput(attrs={'class':'form-control'}),
            'jmbg': forms.TextInput(attrs={'class': 'form-control'}),
            'email_1': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}),
            'email_2': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}),
            'vakcina': forms.Select(attrs={'class': 'form-control'}),
            'bolest_id': forms.Select(attrs={'class':'form-control'}),
            'alergija': forms.CheckboxInput(),

        }

    def clean_jmbg(self):
        data = self.cleaned_data['jmbg']
        for char in data:
            if not char.isdigit():
                self.add_error('jmbg', error="Neispravan JMBG. Maticni broj se sastoji samo od cifara!")
                #raise forms.ValidationError('Neispravan JMBG')
            return data

    def clean(self):
            cleaned_data = super().clean()
            email_1 = cleaned_data.get("email_1")
            email_2 = cleaned_data.get("email_2")

            if email_1 and email_2:
                # Only do something if both fields are valid so far.
                if email_1 != email_2:
                    print("nisu iste adrese")
                    raise forms.ValidationError("Email adrese nisu iste")

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EmailInput(forms.EmailInput):
    input_type = 'email'

class ObavestiForm(forms.Form):
    datum = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}))
    # vreme = forms.TimeField(widget=TimeInput(attrs={'class':'form-control'}))
    ime = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    poruka = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    def clean(self):
            cleaned_data = super().clean()
            datum = datetime.strptime(self.data['datum'], "%Y-%m-%dT%H:%M")
            cleaned_data['datum'] = datetime.strftime(datum, "%d-%m-%Y %H:%M")
            return cleaned_data

    def full_clean(self):
            cleaned_data = super().full_clean()
            if 'datum' in self.errors:
                del self.errors['datum']
            return cleaned_data


class BolestForm(ModelForm):
    class Meta:
        model = Bolest
        fields = "__all__"

        widgets ={
            'ime_bolesti':forms.TextInput(attrs={'class':'form-control'}),
            'ime_doktora':forms.DateInput(attrs={'class':'form-control'}),
        }
