from django.forms import ModelForm
from .models import Card_Box, Deck, Card


class NewCardBoxForm(ModelForm):
    class Meta:
        model = Card_Box
        fields = ('name',)
