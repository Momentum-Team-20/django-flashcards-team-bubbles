from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username


# Model for container holding a deck of cards
class Card_Box(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='card_boxes'
    )

    def __str__(self):

        return self.name


# Model to create a deck of cards
class Deck(models.Model):
    name = models.CharField(max_length=50, null=True)
    num_of_cards = models.IntegerField(blank=True, null=True)
    box = models.ForeignKey(
        'Card_Box', on_delete=models.CASCADE, related_name='decks'
    )

    def __str__(self):

        return self.name


# Model for individual cards
class Card(models.Model):
    name = models.CharField(max_length=50, null=True)
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, related_name='cards'
    )

    def __str__(self):

        return self.name
    