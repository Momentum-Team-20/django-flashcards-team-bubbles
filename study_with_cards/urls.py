from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_home, name='home'),
    path('decks/', views.deck_list, name='deck-list'),
    path('decks/<int:deck_pk>/cards', views.card_list, name="card-list"),
    path('new-card-box/', views.create_new_card_box, name='new-card-box')
]