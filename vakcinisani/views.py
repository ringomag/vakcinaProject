from django.shortcuts import render, redirect
from .models import *
from .forms import VakcinisanForm, ObavestiForm, BolestForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.core import serializers

# Class Based View
class MethodView(View):
    template_name = 'lista.html'
    form = VakcinisanForm
    bolest = BolestForm
    def get(self, request, *args, **kwargs):
        # form = VakcinisanForm
        form = self.form(request.GET)
        bolest = self.bolest(request.GET)
        kreirani = Vakcinisan.objects.all().order_by('-datum')
        return render(request, self.template_name, {'form':form, 'kreirani':kreirani, 'bolest':bolest})

    def post(self, request, *args, **kwargs):
        form = VakcinisanForm
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            # messages
            messages.success(request, 'Uspešno ste se prijavili za vakcinaciju!')
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
        form = ObavestiForm(request.POST)

        if form.is_valid():

            message_name = form.cleaned_data['ime']
            message_content = "datum: " + str(form.cleaned_data['datum']) + " poruka: " + form.cleaned_data['poruka']
            message_from = form.cleaned_data['mail']
            print('dobro je')
            print(message_content)

            # send_mail
            send_mail(
            message_name, #subject
            message_content, #message
            message_from, #from email
            ['optimuskrajm@gmail.com'], #to email
            fail_silently=False,
            )
            return redirect('obavesti')

        return render(request, 'obavesti_korisnika.html', {'form':form, 'message_name':message_name})

# ovo je ajax
def bolest(request):
    if request.method == 'POST':
        form = BolestForm(request.POST)
        if form.is_valid():
            data = form.save()
            print("ovo je data: ", data)
            ser_data = serializers.serialize('json', [data,])
            print("ovo je ser data ", ser_data)
            return JsonResponse({"data": ser_data}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    #some error ocured
    return JsonResponse({"error": ""}, status=400)


#dodavenje nove bolesti
def bolest_lista(request):
    bolesti = Bolest.objects.all().order_by('-id')
    form = BolestForm
    # if request.method == 'POST':
    #     form = BolestForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    return render(request, 'bolest.html', {'bolesti':bolesti, 'form':form})

def detalji_bolest(request, pk):
    bolesti = Bolest.objects.get(id=pk)
    return render(request, 'detalji_bolesti.html', {"bolesti":bolesti})

def izmeni_bolest(request, pk):
    bolesti = Bolest.objects.get(id=pk)
    form = BolestForm(instance=bolesti)
    if request.method == 'POST':
        form = BolestForm(request.POST, instance=bolesti)
        if form.is_valid():
            form.save()
            return redirect('bolest')
    return render(request, 'bolest_edit.html', {'bolesti':bolesti, "form":form})




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
