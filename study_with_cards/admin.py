from django.contrib import admin
from .models import User, Card_Box, Deck, Card

# Register your models here.
admin.site.register(User)
admin.site.register(Card_Box)
admin.site.register(Deck)
admin.site.register(Card)