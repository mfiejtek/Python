while True:
    line = input("Podaj liczbę rzeczywistą (lub 'stop' aby zakończyć): ")
    if line == 'stop':
        break
    try:
        num = float(line)
        print(f"Wprowadziłeś liczbę: {num}")
        print(f"Trzecia potęga tej liczby to: {num ** 3}")
    except ValueError:
        print("To nie jest poprawna liczba rzeczywista. Spróbuj ponownie.")