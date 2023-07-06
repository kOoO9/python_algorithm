def solution(n):
    answer = []
    f = n
    for a in range(2, n+1):
        if n % a == 0:
            for an in answer:
                if a % an == 0:
                    break
            else:
                n /= a
                answer.append(a)
    return answer