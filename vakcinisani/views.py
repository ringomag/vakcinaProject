from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm, ObavestiForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail

# Class Based View
class MethodView(View):
    template_name = 'lista.html'
    form = VakcinisanForm
    def get(self, request, *args, **kwargs):
        # form = VakcinisanForm
        form = self.form(request.GET)
        kreirani = Vakcinisan.objects.all().order_by('-datum')
        return render(request, self.template_name, {'form':form, 'kreirani':kreirani})

    def post(self, request, *args, **kwargs):
        form = VakcinisanForm
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            # messages
            messages.success(request, 'Uspešno ste se prijavili za vakicnaciju!')
            return redirect('lista')
        return render(request, self.template_name, {"form":form})

#class based kad ima pk
class EditVakcinisanView(View):
    template_name = 'vakcinisan.html'
    form = VakcinisanForm
    def get(self, request, pk, *args, **kwargs):
        vakcinisan = Vakcinisan.objects.get(id=pk)
        form = VakcinisanForm(instance=vakcinisan)
        context = {'vakcinisan':vakcinisan, 'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        vakcinisan = Vakcinisan.objects.get(id=pk)
        form = VakcinisanForm(instance=vakcinisan)
        form = self.form(request.POST, instance=vakcinisan)
        if form.is_valid():
            form.save()
            return redirect('lista')
        return render(request, self.template_name, {"form":form})

def home(request):
    return render(request, 'home.html', {})

class ObavestiView(View):
    form = ObavestiForm
    def get(self, request, *args, **kwargs):
        form = ObavestiForm
        return render(request, 'obavesti_korisnika.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form = ObavestiForm
        message_name = request.POST['ime']
        message_content = request.POST['datum']+request.POST['poruka']
        message_from = request.POST['mail']

        #send_mail
        send_mail(
        message_name, #subject
        message_content, #message
        message_from, #from email
        ['optimuskrajm@gmail.com'], #to email
        fail_silently=False,
        )

        return render(request, 'obavesti_korisnika.html', {'form':form, 'message_name':message_name})

# #detalji
# def vakcinisan(request, pk):
#     vakcinisan = Vakcinisan.objects.get(id=pk)
#     context = {'vakcinisan':vakcinisan}
#     return render(request, 'vakcinisan.html', context)
#
# #edit
# def edit(request, pk):
#     vakcinisan = Vakcinisan.objects.get(id=pk)
#     form = VakcinisanForm(instance=vakcinisan)
#     if request.method=="POST":
#         form = VakcinisanForm(request.POST, instance=vakcinisan)
#         if form.is_valid():
#             form.save()
#             return redirect('lista')
#     context = {'vakcinisan':vakcinisan, 'form':form}
#     return render(request, 'edit.html', context)


# def index(request):
#     kreirani = Vakcinisan.objects.all()
#     form = VakcinisanForm
#
#     alergija = Vakcinisan.alergija
#     if request.method == "POST":
#         form = VakcinisanForm(request.POST)
#         # import pdb
#         # pdb.set_trace() #ovo moze da se ubaci, kao debuger, pre cuvanja u bazi
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form, 'kreirani':kreirani}
#     return render(request, 'index.html', context)
#
# def delete(request, id):
#     Vakcinisan.objects.get(id=id).delete()
#     return HttpResponseRedirect('/')



# lista građana koji su izrazili zaintersovanost za vakcinu
# def lista(request):
#     kreirani = Vakcinisan.objects.all()
#     return render(request, 'lista.html', {'kreirani':kreirani})

# ova funkcija je za novog gradjanina koji se prijavljuje za vakcinu
# def novi(request):
#     form = VakcinisanForm
#     if request.method == 'POST':
#         form = VakcinisanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/lista/')
#     return render(request, 'novi_pacijent.html', {'form':form})
