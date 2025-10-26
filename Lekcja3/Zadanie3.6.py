def buildRectangle(rows, cols):
    result = []
    
    horizontal = "+---" * cols + "+\n"
    vertical = "|   " * cols + "|\n"

    result.append(horizontal)
    for _ in range(rows):
        result.append(vertical)
        result.append(horizontal)

    return "".join(result)

size = input("Podaj rozmiar prostokąta (wiersze x kolumny): ").lower()

try:
    rows, cols = map(int, size.split('x'))
    if rows <= 0 or cols <= 0:
        print("Liczby muszą być dodatnie.")
        exit()
    if rows > 100 or cols > 100:
        print("Za duży rozmiar prostokąta.")
        exit()
except ValueError:
    print("Błędny format! Przykład: 2x4")
    exit()

print(buildRectangle(rows, cols))
