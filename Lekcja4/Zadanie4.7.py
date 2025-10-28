def flatten(sequence):
    flattenSequence = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattenSequence.extend(flatten(item))
        else:
            flattenSequence.append(item)
    return flattenSequence
