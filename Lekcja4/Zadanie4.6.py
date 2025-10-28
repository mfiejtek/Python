def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total
