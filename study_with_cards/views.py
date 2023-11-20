from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewCardBoxForm
from .models import User, Card_Box, Card, Deck


# Create your views here.
def user_home(request):
    boxes = Card_Box.objects.all()
    return render(request, 'index.html', {'boxes': boxes})


def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'deck_list.html', {'decks': decks})


def card_list(request, deck_pk):
    cards = Card.objects.filter(deck_id=deck_pk)
    return render(request, 'card_list.html', {'cards': cards})


def create_new_card_box(request):
    card_box = Card_Box.objects.all()
    if request.method == 'POST':
        form = NewCardBoxForm(request.POST)
        new_card_box = form.save(commit=False)
        new_card_box.card_box = card_box
        new_card_box.save()
        return redirect('home')
    form = NewCardBoxForm()
    return render(request, "new_card_box.html", {'form': form})
