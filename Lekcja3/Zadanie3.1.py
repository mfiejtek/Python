#Kod działa, ale zawiera niepotrzebne średniki na końcu linii
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Kod nie działa z powodu błędu składniowego
for i in "axby": if ord(i) < 100: print (i)

#Kod poprawny
for i in "axby": print (ord(i) if ord(i) < 100 else i)