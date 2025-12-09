import random

class KostkaModel:
    def __init__(self):
        self.scianki = {
            1: '\u2680',  # ⚀
            2: '\u2681',  # ⚁
            3: '\u2682',  # ⚂
            4: '\u2683',  # ⚃
            5: '\u2684',  # ⚄
            6: '\u2685'   # ⚅
        }

    def rzut(self):
        wynik = random.randint(1, 6)
        return wynik, self.scianki[wynik]