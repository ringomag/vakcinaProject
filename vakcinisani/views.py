from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm

# Create your views here.
def index(request):
    kreirani = Vakcinisan.objects.all()


    form = VakcinisanForm

    if request.method == "POST":
        form = VakcinisanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form, 'kreirani':kreirani}
    return render(request, 'index.html', context)
