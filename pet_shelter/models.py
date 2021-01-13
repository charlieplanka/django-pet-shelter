from django.db import models


class Pet(models.Model):
    SPECIES_CHOICES = [
        ("Собаки", "Собаки"),
        ("Коты и кошки", "Коты и кошки"),
        ("Кролики", "Кролики")
    ]

    GENDER_CHOICES = [
        ("Ж", "Ж"),
        ("М", "М"),
        ("Неизвестно", "Неизвестно")
    ]

    species = models.CharField(max_length=100, choices=SPECIES_CHOICES, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default="Неизвестно")
    description = models.TextField(blank=True)
    arrival_date = models.DateField(auto_now_add=True)
    breed = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='pet_photos', blank=True)

    def __str__(self):
        return f"{self.species}: {self.name}"
