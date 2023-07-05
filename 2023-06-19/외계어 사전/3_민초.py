def solution(spell, dic):
    answer = 0
    
    for d in dic:
        for s in spell:
            if s not in d:
                answer = 0
                continue
            else:
                answer += 1
                if answer == len(spell):
                    return 1
        answer = 0
    return 2
