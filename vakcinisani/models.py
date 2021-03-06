from django.db import models

class Vakcinisan(models.Model):
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)

    def __str__(self):
        return self.ime + ' ' + self.prezime
