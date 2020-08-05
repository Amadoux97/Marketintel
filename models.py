# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Utilisateur(models.Model):
    nom = models.TextField(db_column='Nom', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    prenom = models.TextField(db_column='Prenom', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)
    estadmin = models.BooleanField(db_column='Estadmin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Utilisateur'


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
