L = [3, 5, 4] ; L = L.sort() # sort() zwraca None
x, y = 1, 2, 3 # za dużo wartości do przypisania
X = 1, 2, 3 ; X[1] = 4 # krotki są niemodyfikowalne
X = [1, 2, 3] ; X[3] = 4 # indeks poza zakresem
X = "abc" ; X.append("d") # łańcuchy nie mają metody append
L = list(map(pow, range(8))) # brak drugiego argumentu dla pow()