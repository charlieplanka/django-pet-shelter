from django.contrib import admin
from pet_shelter.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    @staticmethod
    def pet(self):
        return self
    
    list_display = ('pet', 'gender', 'age')
