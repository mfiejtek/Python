from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Zakładamy, że (x1, y1) to lewy dolny róg, a (x2, y2) to prawy górny
        if x2 <= x1 or y2 <= y1:
            raise ValueError("Niepoprawne współrzędne: (x2, y2) musi być większe od (x1, y1).")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # --- Nowa metoda klasowa ---
    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Wymagana jest lista lub krotka zawierająca dokładnie dwa punkty.")
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):    # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):    # obsługa rect1 != rect2
        return not self == other

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def top(self):
        return self.pt2.y

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def center(self):           # zwraca środek prostokąta jako Point
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):             # pole powierzchni
        return self.width * self.height

    def move(self, x, y):       # przesunięcie o (x, y) 
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self
    
    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być typu Rectangle.")

        # Używamy nowych properties dla czytelności
        x1 = max(self.left, other.left)
        y1 = max(self.bottom, other.bottom)
        x2 = min(self.right, other.right)
        y2 = min(self.top, other.top)
        
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            return None

    def cover(self, other):     # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być typu Rectangle.")
        
        x1 = min(self.left, other.left)
        y1 = min(self.bottom, other.bottom)
        x2 = max(self.right, other.right)
        y2 = max(self.top, other.top)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):            # zwraca krotkę czterech mniejszych
        # Uwaga: self.center jest teraz atrybutem, nie metodą, więc usuwamy ()
        cx, cy = self.center.x, self.center.y
        return (Rectangle(self.left, self.bottom, cx, cy),
                Rectangle(cx, self.bottom, self.right, cy),
                Rectangle(self.left, cy, cx, self.top),
                Rectangle(cx, cy, self.right, self.top))