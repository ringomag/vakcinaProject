from django.db import models

class Vakcinisan(models.Model):
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    vrste_vakcina = (
        ("fajzer","fajzer"),
        ("sputnjk","sputnjik"),
        ("astra zeneka","astra zeneka"),
        ("sinofarm","sinofarm"),
        ("moderna","moderna"),
    )

    vakcina = models.CharField(max_length=100, choices=vrste_vakcina)

    def __str__(self):
        return self.ime + ' ' + self.prezime + ' ' + self.vakcina
