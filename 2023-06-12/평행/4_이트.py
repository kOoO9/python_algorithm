from itertools import combinations
def solution(dots):
    line = []
    for i, dot in enumerate(dots):
        for d in dots[i+1:]:
            line.append([[dot, d], (dot[1]-d[1])/(dot[0]-d[0])])
    for l in line[:3]:
        for ll in line[3:]:
            if [i for i in dots if i not in l[0]] == ll[0]:
                if l[1] == ll[1]:
                    return 1
    return 0