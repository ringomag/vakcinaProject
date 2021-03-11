from django.db import models

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

    vakcina = models.CharField(max_length=100, choices=vrste_vakcina)

    def __str__(self):
        return self.ime + ' ' + self.prezime + ' ' + self.vakcina
