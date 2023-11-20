from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewCardBoxForm, NewDeckForm, NewCardForm
from .models import User, Card_Box, Card, Deck


@login_required
# Create your views here.
def user_home(request):
    boxes = request.user.card_boxes.all()
    return render(request, 'index.html', {'boxes': boxes})

@login_required
def deck_list(request, pk):
    decks = Deck.objects.filter(box__user=request.user, box_id=pk)
    return render(request, 'deck_list.html', {'decks': decks})

@login_required
def card_list(request, deck_pk):
    cards = Card.objects.filter(deck_id=deck_pk)
    return render(request, 'card_list.html', {'cards': cards})

@login_required
def create_new_card_box(request):
    if request.method == 'POST':
        form = NewCardBoxForm(request.POST)
        new_card_box = form.save(commit=False)
        new_card_box.user = request.user
        new_card_box.save()
        return redirect('home')
    form = NewCardBoxForm()
    return render(request, "new_card_box.html", {'form': form})


@login_required
def create_new_deck(request):
    deck = Deck.objects.all()
    if request.method == 'POST':
        form = NewDeckForm(request.POST)
        new_deck = form.save(commit=False)
        new_deck.deck = deck
        new_deck.save()
        return redirect('home')
    form = NewDeckForm()
    return render(request, 'new_deck.html', {'form': form})


@login_required
def create_new_card(request):
    card = Card.objects.all()
    if request.method == 'POST':
        form = NewCardForm(request.POST)
        new_card = form.save(commit=False)
        new_card.card = card
        new_card.save()
        return redirect('home')
    form = NewCardForm()
    return render(request, 'new_card.html', {'form': form})
