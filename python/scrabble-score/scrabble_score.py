pointsMap = {
    'aeioulnrst': 1,
    'dg': 2,
    'bcmp': 3,
    'fhvwy': 4,
    'k': 5,
    'jx': 8,
    'qz': 10
}


def score(word):
    count = {}
    points = 0
    for c in word:
        count.setdefault(c.lower(), 0)
        count[c.lower()] += 1
    for c in count:
        for cs in pointsMap:
            if c in cs:
                points += count[c] * pointsMap[cs]
    return points
