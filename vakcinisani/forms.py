from django.forms import ModelForm
from .models import Vakcinisan
from django import forms

class VakcinisanForm(ModelForm):
    class Meta:
        model = Vakcinisan
        fields = '__all__'
