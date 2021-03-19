from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.views import View

class MethodView(View):
    template_name = 'lista.html'
    form = VakcinisanForm
    def get(self, request, *args, **kwargs):
        form = VakcinisanForm
        kreirani = Vakcinisan.objects.all()
        return render(request, self.template_name, {'form':form, 'kreirani':kreirani})

    def post(self, request, *args, **kwargs):
        form = VakcinisanForm
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
        return render(request, self.template_name, {"form":form})



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
# def lista(request):
#     kreirani = Vakcinisan.objects.all()
#     return render(request, 'lista.html', {'kreirani':kreirani})

# ova funkcija je za novog gradjanina koji se prijavljuje za vakcinu
def novi(request):
    form = VakcinisanForm
    if request.method == 'POST':
        form = VakcinisanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista/')
    return render(request, 'novi_pacijent.html', {'form':form})
