from django.shortcuts import render
from .models import User, Card_Box, Card, Deck


# Create your views here.
def user_home(request):
    boxes = Card_Box.objects.all()
    return render(request, 'index.html', {'boxes': boxes})
