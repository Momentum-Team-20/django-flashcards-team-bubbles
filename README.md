# Django Flashcards

For this project, you will working in pairs to build a more complex Django app that allows users to create flashcards and quiz themselves on them.

## Getting Started

- Set up a new Django project from scratch. There is no starter code in the assignment repo.
- Make sure to create a `.gitignore` file to exclude certain files (like your `.env` file and `db.sqlite3`) from Git. You can get one specific to a Django project at [gitignore.io](https://www.toptal.com/developers/gitignore). Just search for `Django` and copy and paste the text you find there into your `.gitignore` file. It should be placed at the root of your repo, alongside the Pipfile.
- Make sure to create a custom user model, following best practices. **Do this before you run any migrations.** [This guide may be helpful to you.](https://learndjango.com/tutorials/django-custom-user-model)
- You may want to install `django-debug-toolbar`, `django-extensions`, and `django-environ`.

## Stretch goal for each project: trying new things

Teams should consider trying something they don't know how to do on their project. This could be a Python or JavaScript library they haven't used before or a feature of Django they haven't tried.

## Project Requirements

You want to make an application to help people learn via flashcards. Some great examples of this on the web are [Julia Evan's questions](https://questions.wizardzines.com/) and [Nicky Case's How to Remember Anything Forever-ish](https://ncase.me/remember/). You DO NOT need to replicate either of those examples, but they may help you visualize how a user may interact with your app and inspire you with ideas.

Your app will need login and registration. You'll use `django-registration-redux` which works with Django's built-in authentication system and Django's built-in user model.

- Logged in users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Logged in users can see a list of their decks.
- Logged in users can select a deck to begin a quiz on the cards in the deck.
- The quiz should show the user a card. The user can click to see the answer. The user can mark whether or not they got the answer correct.

Your application should be styled. It should be usable and aesthetically neutral, at a minimum. You can use a library or you can write custom css, or both. It is up to you.

### How decks and cards work

A user can have multiple decks of flashcards. Each deck has a title. Each flash card has a prompt or question and an answer.

When a user is quizzing themselves on a deck, they _do not_ have to type in answers. They are shown the prompt, they click to see the answer; they then mark whether they answered it correctly or not. They should see one card at a time.

When the user marks success or failure on a card, this should be recorded.

The cards should be shown in a random order at a minimum. A preferable method would be to use something like [the Leitner system](https://www.virtualsalt.com/learn10.html) for flash cards. This system uses review times; you could use that, or just use the idea of multiple boxes, with cards in lower boxes coming up more often.

### Creating decks and running through decks

This application has two very distinct parts: creating decks and cards and then running through those decks. This is a natural place to split work. Do not forget to make creating decks and cards an easy-to-use experience.

### How much of this is JavaScript?

"Flipping" a card (you don't have to animate a card flip, although if you do, that's very cool) will almost certainly require JavaScript.

You could have a page load in between cards and reduce your amount of JavaScript. Depending on how you do this, it could also record success or failure, eliminating most of your JavaScript.
