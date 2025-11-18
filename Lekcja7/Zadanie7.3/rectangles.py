from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x2 <= x1 or y2 <= y1:
            raise ValueError("Niepoprawne współrzędne: (x2, y2) musi być większe od (x1, y1).")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):    # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2) or (self.pt1 == other.pt2 and self.pt2 == other.pt1) 
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):             # pole powierzchni
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y):     # przesunięcie o (x, y) 
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self
    
    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być typu Rectangle.")

        x1 = max(min(self.pt1.x, self.pt2.x), min(other.pt1.x, other.pt2.x))
        y1 = max(min(self.pt1.y, self.pt2.y), min(other.pt1.y, other.pt2.y))
        x2 = min(max(self.pt1.x, self.pt2.x), max(other.pt1.x, other.pt2.x))
        y2 = min(max(self.pt1.y, self.pt2.y), max(other.pt1.y, other.pt2.y))
        
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            return None

    def cover(self, other):     # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być typu Rectangle.")
        
        x1 = min(self.pt1.x, self.pt2.x, other.pt1.x, other.pt2.x)
        y1 = min(self.pt1.y, self.pt2.y, other.pt1.y, other.pt2.y)
        x2 = max(self.pt1.x, self.pt2.x, other.pt1.x, other.pt2.x)
        y2 = max(self.pt1.y, self.pt2.y, other.pt1.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):            # zwraca krotkę czterech mniejszych
        cx, cy = self.center().x, self.center().y
        return (Rectangle(self.pt1.x, self.pt1.y, cx, cy),
                Rectangle(cx, self.pt1.y, self.pt2.x, cy),
                Rectangle(self.pt1.x, cy, cx, self.pt2.y),
                Rectangle(cx, cy, self.pt2.x, self.pt2.y))
