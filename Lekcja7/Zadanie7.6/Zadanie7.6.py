# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import itertools
import random

# (a)
def iterator_a():
    while True:
        yield 0
        yield 1

it_a = iterator_a()
for _ in range(10):
    print(next(it_a), end=' ')
print()

# (b)
def iterator_b():
    directions = ("N", "E", "S", "W")
    while True:
        yield random.choice(directions)

it_b = iterator_b()
for _ in range(10):
    print(next(it_b), end=' ')
print()

# (c)
def iterator_c():
    days = itertools.cycle(range(7))
    for day in days:
        yield day
        
it_c = iterator_c()
for _ in range(14):
    print(next(it_c), end=' ')
print()
