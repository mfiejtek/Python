# Stałe dla kolorów
RED = 1
BLACK = 0

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = RED
