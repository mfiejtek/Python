def factorial(n):
    if n < 0:
        raise ValueError("n musi być dodatnie")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

