from django.db import models

class Entreprise(models.Model):
    nom = models.TextField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    pays = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    secteur = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entreprise'


# Create your models here.
