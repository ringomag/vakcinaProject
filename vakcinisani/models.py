import uuid
from django.db import models
from django import forms


class Vakcinisan(models.Model):
    #pokusao sa id uuid, ali onda mi se sve pojebe, ne mogu da pristupim ni bazi preko admina
    #mozda zato sto sam vec imao dosta kreiranih i dosta izmena u bazi...
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    vrste_vakcina = (
        ("Fajzer","Fajzer"),
        ("Sputnjik","Sputnjik"),
        ("Astra Zeneka","Astra Zeneka"),
        ("Sinofarm","Sinofarm"),
        ("Moderna","Moderna"),
    )
    jmbg = models.CharField(max_length=13, blank=True)
    vakcina = models.CharField(max_length=100, choices=vrste_vakcina)
    alergija = models.BooleanField(default=False)
    datum = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ime + ' ' + self.prezime + ' ' + self.vakcina
