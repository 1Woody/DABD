from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# fabricant
class Fabricant(models.Model):
    nom = models.CharField(max_length=30, primary_key=True)
    loc_headquarters = models.CharField(max_length=30)
    num_treballadors = models.PositiveIntegerField()
    pressupost = models.PositiveIntegerField() #limitats a 200M

    def __str__(self):
       return self.nom

#Team Principal
class TeamPrincipal (models.Model):
    dni = models.CharField(max_length=9, validators=[RegexValidator(regex='^.{9}$', message='Length has to be 9', code='nomatch')], primary_key=True)
    nom = models.CharField(max_length=40)
    telefon = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    edat = models.PositiveIntegerField(validators=[MaxValueValidator(140)])
    nacionalitat = models.CharField(max_length=20)

    def __str__(self):
       return self.dni


#Pilot
class Pilot (models.Model):
    dni = models.CharField(max_length=9, validators=[RegexValidator(regex='^.{9}$', message='Length has to be 9', code='nomatch')], primary_key=True)
    nom = models.CharField(max_length=40)
    telefon = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])
    edat = models.PositiveIntegerField(validators=[MaxValueValidator(140)])
    nacionalitat = models.CharField(max_length=20, default="")

    def __str__(self):
       return self.dni

#Gran Premi
class GranPremi (models.Model):
    nom = models.CharField(max_length=30, primary_key=True)
    localització = models.CharField(max_length=30)
    longitud = models.PositiveIntegerField()
    durada = models.PositiveIntegerField(validators=[MaxValueValidator(15000)]) #minuts
    voltes = models.PositiveIntegerField(validators=[MaxValueValidator(999)]) #limitats a 200M

    def __str__(self):
       return self.nom

#Temporada
class Temporada (models.Model):
    any = models.PositiveIntegerField(validators=[RegexValidator(regex='^\w{4}$', message='Length has to be 4', code='nomatch')], primary_key=True)
    # modificar por rango
    
    def __int__(self):
       return self.any

#Mundial de pilots
class MundialPilot (models.Model):
    punts = models.PositiveIntegerField(validators=[MaxValueValidator(1000)], primary_key=True)

    def __int__(self):
       return self.punts


#Mundial de Fabricants
class MundialFabricant (models.Model):
    punts = models.PositiveIntegerField(validators=[MaxValueValidator(1000)], primary_key=True)
    # faltan foreign keys

    def __int__(self):
       return self.punts

#Resultats Gran Premi
class Resultat (models.Model):
    punts = models.PositiveIntegerField(validators=[MaxValueValidator(25)], primary_key=True)
    # faltan foreign keys

    def __int__(self):
       return self.punts


#VALIDATORS 

#from django.core.validators import MaxValueValidator
#
#class MyModel(models.Model):
#    ...
#    id_student = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])

#from django.db import models
#from django.core.validators import MinValueValidator, MaxValueValidator
#
#size = models.IntegerField(validators=[MinValueValidator(0),
#                                       MaxValueValidator(5)])