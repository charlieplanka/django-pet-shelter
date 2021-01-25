from django import forms
from .models import Pet


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = "__all__"
        labels = {
            "specie": "Вид питомца",
            "name": "Имя",
            "age": "Возраст",
            "gender": "Пол",
            "description": "Описание",
            "breed": "Порода",
            "photo": "Фото",
        }
