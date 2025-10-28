
def make_ruler(n):
    dotsnlines = "|"
    numbers = "0"
    if(n <= 0):
        print("Długość miarki musi być liczbą całkowitą dodatnią.")
        exit(0)
    elif(n > 999):
        print("Długość miarki jest zbyt duża.")
        exit(0)
    for i in range(1, n + 1):
        dotsnlines += "....|"
        numbers += " "*(5-len(str(i))) + str(i)
    outputString = dotsnlines + "\n" + numbers
    return outputString 


def make_grid(rows, cols):
    try:
        if rows <= 0 or cols <= 0:
            print("Liczby muszą być dodatnie.")
            exit()
    except ValueError:
        print("Błędne dane!")
        exit()

    result = []
    
    horizontal = "+---" * cols + "+\n"
    vertical = "|   " * cols + "|\n"

    result.append(horizontal)
    for _ in range(rows):
        result.append(vertical)
        result.append(horizontal)

    return "".join(result)

