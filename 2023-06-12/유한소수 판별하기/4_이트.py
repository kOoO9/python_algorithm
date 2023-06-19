def fac(x):
    answer = []
    d = 2
    while d <= x:
        if x % d == 0:
            answer.append(d)
            x = x / d
        else:
            d = d + 1
    return answer

def solution(a, b):
    al = fac(a)
    if al != None:
        alc = al.copy()
        for i in al:
            if b % i == 0:
                alc.remove(i)
                b /= i
    if [i for i in fac(b) if i not in {2, 5}] != []:
        return 2
    else:
        return 1