from tkinter import *
class Draggable:
    def add_draggable(self, widget):
        widget.bind('<ButtonPress-1>', self.on_start)
        widget.bind('<B1-Motion>', self.on_drag)
        widget.bind('<ButtonRelease-1>', self.on_drop)

    def on_start(self, thing):
        print("clicked")

    def on_drag(self, thing):
        print("dragged")
    def on_drop(self, thing):
        print("dropped")
        x, y = thing.widget.winfo_pointerxy()
        new_pos = thing.widget.winfo_containing(x, y)
        new_pos.configure(image=PhotoImage(file="DeckOfCards\\c2.png"))
