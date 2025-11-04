from math import gcd

def reduce_frac(frac):
    top, bot = frac
    if bot == 0:
        raise ZeroDivisionError("Mianownik nie może być równy zero")
    
    if bot < 0:
        top = -top
        bot = -bot
    
    g = gcd(top, bot)
    return [top/g, bot/g]

def add_frac(frac1, frac2):
    top = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    bot = frac1[1] * frac2[1]
    return reduce_frac([top, bot])

def sub_frac(frac1, frac2): 
    top = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    bot = frac1[1] * frac2[1]
    return reduce_frac([top, bot])

def mul_frac(frac1, frac2):
    return reduce_frac([frac1[0]*frac2[0], frac1[1]*frac2[1]])

def div_frac(frac1, frac2):
    if frac2[0] == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    top = frac1[0] * frac2[1]
    bot = frac1[1] * frac2[0]
    return reduce_frac([top, bot])

def is_positive(frac):
    return (frac[0] >= 0 and frac[1] >= 0)

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    left = frac1[0] * frac2[1]
    right = frac2[0] * frac1[1]
    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0

def frac2float(frac):
    return frac[0]/frac[1]