import tkinter as tk
from model import KostkaModel
from view import KostkaView

class Aplikacja(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Symulator Rzutu Kostką")
        self.geometry("400x350")
        self.resizable(False, False)

        self.model = KostkaModel()
        self.view = KostkaView(self)

        self.view.ustaw_akcje_przycisku(self.wykonaj_rzut)

    def wykonaj_rzut(self):
        wartosc, symbol = self.model.rzut()
        self.view.zaktualizuj_wynik(symbol, wartosc)