def solution(s):
    answer = 0
    sl = s.split(' ')
    for i, n in enumerate(sl):
        if n == 'Z':
            answer -= int(sl[i-1])
        else:
            answer += int(sl[i])
    return answer