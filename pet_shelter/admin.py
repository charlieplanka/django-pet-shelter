from django.contrib import admin
from pet_shelter.models import Pet, Specie


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    @staticmethod
    def pet(self):
        return self

    list_display = ('pet', 'gender', 'age', 'breed', 'arrival_date')


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    pass
