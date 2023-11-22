from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewCardBoxForm, NewDeckForm, NewCardForm, AnswerBoxForm, CardForm
from .models import User, Card_Box, Card, Deck
import random


# function to compile list of cards in a given deck



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
    if request.method == 'POST':
        card = random.choice(cards)
        card_pk = card.pk
        return card_question(request, card_pk)
    return render(request, 'card_list.html', {'cards': cards, 'deck_pk': deck_pk})

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


@login_required
def card_details(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        form = AnswerBoxForm(request.POST, instance=card)
        form.save()
        deck_pk = card.deck_id
        cards = Card.objects.filter(deck_id=deck_pk)
        new_card = random.choice(cards)
        new_pk = new_card.pk
        return card_question(request, new_pk)
    form = AnswerBoxForm(instance=card)
    return render(request, 'card_details.html', {'card': card, 'form': form})


@login_required
def update_card(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        form = NewCardForm(request.POST, instance=card)
        card = form.save(commit=False)
        card.save()
        return redirect('home')
    form = NewCardForm(instance=card)
    return render(request, 'update_card.html', {'form': form})


def card_question(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    return render(request, 'card_question.html', {'card': card})


# delete function for cards
def delete_card(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        card = form.save(commit=False)
        card.delete()
        return redirect('home',)
    form = CardForm(instance=card)
    return render(request, 'delete_card.html', {'form': form})


def delete_deck(request, deck_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'POST':
        form = NewDeckForm(request.POST, instance=deck)
        deck = form.save(commit=False)
        deck.delete()
        return redirect('home',)
    form = NewDeckForm(instance=deck)
    return render(request, 'delete_deck.html', {'form': form})
