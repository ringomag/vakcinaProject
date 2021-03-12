from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    kreirani = Vakcinisan.objects.all()
    form = VakcinisanForm

    alergija = Vakcinisan.alergija
    if request.method == "POST":
        form = VakcinisanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'kreirani':kreirani}
    return render(request, 'index.html', context)




def delete(request, id):
    Vakcinisan.objects.get(id=id).delete()
    return HttpResponseRedirect('/')
