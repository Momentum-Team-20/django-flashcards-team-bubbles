from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_home, name='home'),
    path('decks/<int:pk>/', views.deck_list, name='deck-list'),
    path('decks/<int:deck_pk>/cards', views.card_list, name="card-list"),
    path('new-card-box/', views.create_new_card_box, name='new-card-box'),
    path('new-deck/', views.create_new_deck, name="new-deck"),
    path('new-card/', views.create_new_card, name='new-card'),
    path('card/<int:card_pk>/', views.card_details, name='card-details'),
    path('card/<int:card_pk>/update',views.update_card, name='update-card' ),
    path('card/<int:card_pk>/question', views.card_question, name='card-question'),
]