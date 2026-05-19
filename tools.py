def is_fuzzy_match(a, b):
    if a == b:
        return True

    len_a, len_b = len(a), len(b)

    # If the difference in length is more than 2, return false
    if abs(len_a - len_b) > 2:
        return False

    # If one string is longer than the other, swap them
    if len_a > len_b:
        a, b = b, a
        len_a, len_b = len_b, len_a

    best_match = 0

    # Check if the shorter string is a substring of the longer string
    for i in range(len_b - len_a + 1):
        match = 0

        # Check if the characters match
        for j in range(len_a):
            if a[j] == b[i + j]:
                match += 1

        # Update the best match
        best_match = max(best_match, match)

    # Calculate the similarity score
    similarity = best_match / len_a

    return similarity >= 0.75