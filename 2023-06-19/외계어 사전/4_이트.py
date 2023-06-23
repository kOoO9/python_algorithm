def solution(spell, dic):
    for d in dic:
        a = 0
        for s in spell:
            if s in d:
                a += 1
        if a == len(spell):
            return 1          
    return 2