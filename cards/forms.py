from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Deck, Flashcard


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password",
        })
    )


class DeckForm(forms.ModelForm):
    class Meta:
        model=Deck
        fields=["name","description"]


class FlashcardForm(forms.ModelForm):
    class Meta:
        model=Flashcard
        fields=["deck","question","answer"]