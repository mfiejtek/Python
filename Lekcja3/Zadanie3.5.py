dotsnlines = "|"
numbers = "0"

lenOfMeasure = int(input("Podaj długość miarki: "))
if(lenOfMeasure <= 0):
    print("Długość miarki musi być liczbą całkowitą dodatnią.")
    exit(0)
elif(lenOfMeasure > 999):
    print("Długość miarki jest zbyt duża.")
    exit(0)
for i in range(1, lenOfMeasure + 1):
    dotsnlines += "....|"
    numbers += " "*(5-len(str(i))) + str(i)

outputString = dotsnlines + "\n" + numbers
print(outputString)
