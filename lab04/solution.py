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
def ranking(names: list[str], scores: list[float]) -> list[str]:
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return [names[i] for i in order]
