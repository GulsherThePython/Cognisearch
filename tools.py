def is_fuzzy_match(a, b):
    # If they are identical, they are a match
    if a == b:
        return True

    # If the lengths are too different, they are not a match
    if abs(len(a) - len(b)) > 2:
        return False

    # check character overlap
    common = 0
    for char in a:
        if char in b:
            common += 1
    
    # Compute the fraction of characters that overlap to the length of the longer word
    char_overlap_similarity = common / (len(a) if len(a) > len(b) else len(b))

    return char_overlap_similarity > 0.7

    # TODO: Implement Bigram fuzzy matching as well
