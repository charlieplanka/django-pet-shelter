from django.db import models


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("Dog", "Dog"),
        ("Cat", "Cat"),
        ("Rabbit", "Rabbit")
    ]

    GENDER_CHOICES = [
        ("F", "Female"),
        ("M", "Male"),
        ("Unknown", "Unknown")
    ]

    species = models.CharField(max_length=100, choices=SPECIES_CHOICES, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default="Unknown")
    description = models.TextField(blank=True)
    arrival_date = models.DateField(auto_now_add=True)
    breed = models.CharField(max_length=200, blank=True)
    # add photo field

    def __str__(self):
        return f"{self.species} {self.name}"
