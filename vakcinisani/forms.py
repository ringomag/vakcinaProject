from django.forms import ModelForm
from .models import Vakcinisan

class VakcinisanForm(ModelForm):
    class Meta:
        model = Vakcinisan
        fields = '__all__'
