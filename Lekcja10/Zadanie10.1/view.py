import tkinter as tk

class KostkaView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(pady=20, padx=20, fill="both", expand=True)
        self.stworz_interfejs()

    def stworz_interfejs(self):
        self.lbl_wynik = tk.Label(
            self, 
            text="\u2753", 
            font=("Arial", 100), 
            fg="#333333"
        )
        self.lbl_wynik.pack(pady=20)

        self.lbl_opis = tk.Label(
            self, 
            text="Naciśnij przycisk, aby rzucić", 
            font=("Arial", 12)
        )
        self.lbl_opis.pack(pady=10)

        self.btn_rzut = tk.Button(
            self, 
            text="Rzuć kostką!", 
            font=("Arial", 14, "bold"),
            bg="#4CAF50", 
            fg="white",
            cursor="hand2"
        )
        self.btn_rzut.pack(ipadx=10, ipady=5)

    def zaktualizuj_wynik(self, symbol, wartosc):
        self.lbl_wynik.config(text=symbol)
        self.lbl_opis.config(text=f"Wyrzucono: {wartosc}")

    def ustaw_akcje_przycisku(self, funkcja):
        self.btn_rzut.config(command=funkcja)