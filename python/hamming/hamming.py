def distance(strand_a, strand_b):
    difference = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Lenth of strands must be equal.")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            difference += 1
    return difference
