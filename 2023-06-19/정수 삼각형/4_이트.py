def solution(triangle):
    lst = [[] for _ in range(len(triangle))]
    n = len(triangle) - 1
    lst[-1] = triangle[-1]
    while True:
        for i in range(n):
            lst[n-1].append(triangle[n-1][i] + max(lst[n][i:i+2]))
        n -= 1
        if n < 0:
            break
    return lst[0][0]