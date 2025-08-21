from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='specialites/')
    categorie = models.CharField(max_length=50, choices=[
        ('entrée', 'Entrée'),
        ('plat', 'Plat'),
        ('dessert', 'Dessert')
    ])
    prix = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nom
