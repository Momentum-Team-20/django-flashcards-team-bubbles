from django.db import models


# Create your models here.
# Model for container holding a deck of cards
class Card_Box(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):

        return self.name


# Model to create a deck of cards
class Deck(models.Model):
    name = models.CharField(max_length=50, null=True)
    num_of_cards = models.IntegerField(blank=True, null=True)
    box = models.ForeignKey(
        'Card_Box', on_delete=models.CASCADE, related_name='box'
    )

    def __str__(self):

        return self.name


# Model for individual cards
class Card(models.Model):
    name = models.CharField(max_length=50, null=True)
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, related_name='deck'
    )

    def __str__(self):

        return self.name
