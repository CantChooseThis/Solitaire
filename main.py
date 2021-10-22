from tkinter import ttk
from tkinter import *
from card import Card
from card import Deck
from PIL import Image, ImageTk
from draggable import Draggable
root = Tk()
dnd = Draggable()

dp = Deck("Deck")
fds = [Deck("Pile"), Deck("Pile"), Deck("Pile"), Deck("Pile")]
tableau = [Deck("Pile"), Deck("Pile"), Deck("Pile"), Deck("Pile"), Deck("Pile"), Deck("Pile"), Deck("Pile")]
cardstoadd = 1
for pile in tableau:
    pile.add([dp.deal() for card in range(cardstoadd)])
    cardstoadd += 1
    for card in pile.cards:
        card.visible = False
    pile.cards[0].visible = True
dp.cards[0].visible = False
for card in dp.cards:
     if card.visible:
         print("Mistake")

def drag(card, fd):
    if len(fd.cards) != 0:
        top = fd.cards[0]
        if top.suit == card.suit and card.value == top.value+1:
            fd.add([card])
            return True
    else:
        if card.value == 1:
            fd.add([card])
            return True
    return False
canvas = Canvas(root, height=900, width=1200)
canvas.grid()
empty = PhotoImage(file="DeckOfCards\emptypile.png")
empty = empty.subsample(4, 4)
for x in range(7):
    canvas.create_image(150 + x * 150, 300 + (len(tableau[x].cards) - x) * 50, image=empty)
    for y in reversed(range(x+1)):

        # if tableau[x].cards[y].visible:
        tableau[x].cards[y].image()
        canvas.create_image(150+x*150, 300+(len(tableau[x].cards)-y)*50, image=tableau[x].cards[y].image)
        # root.after(1000)
canvas.create_image(150, 100, image=empty)
for card in reversed(dp.cards):
    card.image()
    canvas.create_image(150, 100, image = card.image)
for x in range(5):
    canvas.create_image(300+x*150, 100, image=empty)
# cardholder = Label(canvas, image=tableau[0].cards[0].image)
# cardholder.pack()
# cardholder.place(x=150, y=300)
# dnd.add_draggable(cardholder)
canvas.move(tableau[0].cards[0].image, 0, 200)
root.mainloop()
