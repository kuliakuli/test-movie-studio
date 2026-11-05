from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = [
            "title",
            "year",
            "genre",
            "budget",
            "description",
            "director",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Название фильма"
            }),
            "year": forms.NumberInput(attrs={
                "min": 1888,
                "max": 2100
            }),
            "genre": forms.TextInput(attrs={
                "placeholder": "Например: Фантастика"
            }),
            "budget": forms.NumberInput(attrs={
                "min": 0,
                "step": "0.01"
            }),
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Описание фильма"
            }),
        }
