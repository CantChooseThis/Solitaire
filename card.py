import random as r
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import *

class Card:
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
        self.visible = False
        if self.suit == "Clubs" or self.suit == "Spades":
            self.color = "Black"
        elif self.suit == "Hearts" or self.suit == "Diamonds":
            self.color = "Red"

    def image(self):
        image = 0
        if self.visible:
            token = 0
            if self.number == 1:
                token = "a"
            elif self.number == 11:
                token = "j"
            elif self.number == 12:
                token = "q"
            elif self.number == 13:
                token = 'k'
            else:
                token = self.number
            self.image = PhotoImage(file=f"DeckOfCards\\{self.suit[0].lower()}{token}.png")
            self.image = self.image.subsample(4, 4)
        else:
            self.image = PhotoImage(file="DeckOfCards\\transparentcardback.png")
            self.image = self.image.subsample(4, 4)


class Deck:
    def __init__(self, mode):
        self.cards = []
        if mode == "Deck":
            for x in range(1,14):
                self.cards.append(Card(x, "Hearts"))
                self.cards.append(Card(x, "Diamonds"))
                self.cards.append(Card(x, "Spades"))
                self.cards.append(Card(x, "Clubs"))
            self.shuffle()
    def add(self, cards):
        for card in cards:
            counter = 0
            self.cards.insert(counter, card)
            counter += 1
    def deal(self):
        if len(self.cards) > 1:
            self.cards[1].visible = True
        if len(self.cards) >= 1:
            self.cards[0].visible = True
            return self.cards.pop(0)

    def shuffle(self):
        r.shuffle(self.cards)



