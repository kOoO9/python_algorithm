def solution(n):
    answer = []
    i = 1
    while True:
        if n == len(answer):
            break
        if (i % 3 == 0) or (str(3) in str(i)):
            i += 1
        else:
            answer.append(i)
            i += 1
    return answer[-1]