def odwracanieIteracja(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        right -= 1
        left += 1
    return L


def odwracanieRekurencyjne(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanieRekurencyjne(L, left + 1, right - 1)
    
    return L
