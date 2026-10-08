def winner(names: list[str], scores: list[float]) -> str:
    if not scores:
        return ""

    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i

    return names[best]


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0

    return round(sum(scores) / len(scores), 2)
