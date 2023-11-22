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


class NewCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'question', 'answer', 'deck')


class AnswerBoxForm(ModelForm):
    class Meta:
        model = Card
        fields = ('is_correct',)
        labels = {
            "is_correct": ("Answered Correctly"),
        }
