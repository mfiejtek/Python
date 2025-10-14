#Zadanie 2.10
line = """Mamy dany string wielowierszowy line. 
Podać sposób            obliczenia     liczby
 wyrazów w        stringu. 
 Przez wyraz   rozumiemy ciąg "czarnych" 
 znaków, oddzielony od innych wyrazów 
 białymi znakami      (spacja, tabulacja, newline).  GvR"""

print("### Zadanie 2.10 ###\nLiczba wyrazów w stringu:", len(line.split()))

#Zadanie 2.11
word = "Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia."
print("### Zadanie 2.11 ###\n"+"_".join(word))

#Zadanie 2.12
first_chars = "".join([x[0] for x in line.split()])
last_chars = "".join([x[-1] for x in line.split()])
print("### Zadanie 2.12 ###\nPierwsze znaki wyrazów:", first_chars, "\nOstatnie znaki wyrazów:", last_chars)

#Zadanie 2.13
sum_of_len = sum(len(x) for x in line.split())
print("### Zadanie 2.13 ###\nSuma długości wyrazów:", sum_of_len)

#Zadanie 2.14
longest_word = max(line.split(), key=len)
longest_length = len(longest_word)
print("### Zadanie 2.14 ###\nNajdłuższy wyraz:", longest_word, "\nDługość najdłuższego wyrazu:", longest_length)

#Zadanie 2.15
L = [12321, 13241, 54325234, 1234, 54323, 8678, 34324, 645645, 23432, 1234321]
digits_string = "".join(str(num) for num in L)
print("### Zadanie 2.15 ###\nCiąg cyfr kolejnych liczb:", digits_string)

#Zadanie 2.16
line_gvr = line.replace("GvR", "Guido van Rossum")
print("### Zadanie 2.16 ###\n", line_gvr)

#Zadanie 2.17
line_split = line.split()
sorted_alpha = sorted(line_split)
sorted_length = sorted(line_split, key=len)
print("### Zadanie 2.17 ###\nWyrazy alfabetycznie:", sorted_alpha)
print("Wyrazy wg długości:", sorted_length)

#Zadanie 2.18
big_int = 1010100234023103401230004123040123400024560000063045603450000005203450234054320543000000000000000000053450003450450053400
print("### Zadanie 2.18 ###\nLiczba zer:", str(big_int).count('0'))

#Zadanie 2.19
L = [1, 23, 456, 7, 89, 0, 234, 56, 789]
len_three_nums = [str(num).zfill(3) for num in L]
print("### Zadanie 2.19 ###\nCiąg trzycyfrowych bloków:", "".join(len_three_nums))