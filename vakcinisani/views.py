from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def index(request):
    kreirani = Vakcinisan.objects.all()
    form = VakcinisanForm

    alergija = Vakcinisan.alergija
    if request.method == "POST":
        form = VakcinisanForm(request.POST)
        # import pdb
        # pdb.set_trace() #ovo moze da se ubaci, kao debuger, pre cuvanja u bazi
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'kreirani':kreirani}
    return render(request, 'index.html', context)

def delete(request, id):
    Vakcinisan.objects.get(id=id).delete()
    return HttpResponseRedirect('/')



# lista građana koji su izrazili zaintersovanost za vakcinu
def lista(request):
    kreirani = Vakcinisan.objects.all()
    return render(request, 'lista.html', {'kreirani':kreirani})

# ova funkcija je za novog gradjanina koji se prijavljuje za vakcinu
def novi(request):
    form = VakcinisanForm
    if request.method == 'POST':
        form = VakcinisanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista/')
    return render(request, 'novi_pacijent.html', {'form':form})
