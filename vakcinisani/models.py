from django.db import models
from django import forms

class Vakcinisan(models.Model):
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    vrste_vakcina = (
        ("Fajzer","Fajzer"),
        ("Sputnjik","Sputnjik"),
        ("Astra Zeneka","Astra Zeneka"),
        ("Sinofarm","Sinofarm"),
        ("Moderna","Moderna"),
    )
    jmbg = models.IntegerField()
    vakcina = models.CharField(max_length=100, choices=vrste_vakcina)
    alergija = models.BooleanField(default=False)
    datum = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ime + ' ' + self.prezime + ' ' + self.vakcina
