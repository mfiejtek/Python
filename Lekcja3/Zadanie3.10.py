roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman2int(s):
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman_numerals[char]``
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Przykłady użycia
assert roman2int("XIV") == 14
assert roman2int("MCMXCIV") == 1994
assert roman2int("LVIII") == 58
assert roman2int("MMXXIV") == 2024
print(roman2int("XIV"))
print(roman2int("MCMXCIV"))
print(roman2int("LVIII"))
print(roman2int("MMXXIV"))

# Inny sposób tworzenia słownika
roman_numerals_alt = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

# Sprawdzenie, czy oba słowniki są takie same 
assert roman_numerals == roman_numerals_alt