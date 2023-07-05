def solution(numbers, target):
    nn = [[] for _ in numbers]
    nn[0].extend([numbers[0], -numbers[0]])
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        for prev in nn[i-1]:
            nn[i].extend([prev+n, prev-n])
    return nn[-1].count(target)