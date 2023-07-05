def solution(numbers):
    p, n = [], []
    for num in numbers:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
    m = -float('inf')
    if len(p) >= 2:
        p.sort()
        m = max(m, p[-1] * p[-2])
    if len(n) >= 2:
        n.sort()
        m = max(m, n[0] * n[1])
    if len(p) < 2 and len(n) < 2:
        m = max(m, numbers[0] * numbers[1])
    return m