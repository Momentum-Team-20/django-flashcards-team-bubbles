from django.forms import ModelForm
from .models import Card_Box, Deck, Card


class NewCardBoxForm(ModelForm):
    class Meta:
        model = Card_Box
        fields = ('name',)


class NewDeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ('name', 'box')
