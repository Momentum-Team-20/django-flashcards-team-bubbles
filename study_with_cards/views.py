from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewCardBoxForm
from .models import User, Card_Box, Card, Deck


@login_required
def user_home(request):
    # if not request.user.is_authenticated:
    # redirect to login page if user is not logged in
    # use the logged in user to filter the query
    boxes = Card_Box.objects.filter(user=request.user)
    # boxes = request.user.card_boxes.all()
    return render(request, "index.html", {"boxes": boxes})


@login_required
def deck_list(request):
    decks = Deck.objects.all()
    return render(request, "deck_list.html", {"decks": decks})


def card_list(request, deck_pk):
    cards = Card.objects.filter(deck_id=deck_pk)
    return render(request, "card_list.html", {"cards": cards})


@login_required
def create_new_card_box(request):
    if request.method == "POST":
        form = NewCardBoxForm(request.POST)
        new_card_box = form.save(commit=False)
        new_card_box.user = request.user  # add the logged in user
        # new_card_box.card_box = card_box
        new_card_box.save()
        return redirect("home")
    form = NewCardBoxForm()
    return render(request, "new_card_box.html", {"form": form})
