from django.db import models


class Specie(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Pet(models.Model):
    GENDER_CHOICES = [
        ("Ж", "Ж"),
        ("М", "М"),
        ("Неизвестно", "Неизвестно")
    ]

    specie = models.ForeignKey('Specie', blank=True, null=True, on_delete=models.SET_NULL, related_name='pets')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default="Неизвестно")
    description = models.TextField(blank=True)
    arrival_date = models.DateField(auto_now_add=True)
    breed = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='pet_photos', blank=True)

    def __str__(self):
        return f"{self.specie}: {self.name}"
