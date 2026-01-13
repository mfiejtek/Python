"""Moduł definiujący węzeł drzewa czerwono-czarnego.

Zawiera stałe kolorów `RED` / `BLACK` oraz klasę `Node` przechowującą
pola potrzebne do budowy drzewa (wartość, rodzic, lewe/prawe dziecko, kolor).
"""

# Stałe dla kolorów
RED = 1
BLACK = 0

class Node:
    """Reprezentuje pojedynczy węzeł drzewa.

    Atrybuty:
        val: przechowywana wartość klucza
        parent, left, right: wskaźniki na inne węzły
        color: kolor węzła (`RED` lub `BLACK`)
    """
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = RED
