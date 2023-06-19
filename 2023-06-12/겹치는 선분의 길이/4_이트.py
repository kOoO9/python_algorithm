def dup(lines):
    answer = []
    lines.sort()
    for i, line in enumerate(lines):
        for j in lines[i+1:]:
            if line[1] >= j[0]:
                if line[1] >= j[1]:
                    answer.append([j[0], j[1]])
                else:
                    answer.append([j[0], line[1]])
    return answer

def solution(lines):
    answer, i = 0, 0
    dupl = dup(lines)
    dupl.sort()
    while True:
        try:
            dupl1, dupl2 = dupl[i], dupl[i+1]
        except:
            break
        if dupl1[1] >= dupl2[0]:
            dupl.remove(dupl1)
            dupl.remove(dupl2)
            dupl.append([dupl1[0], dupl2[1]])
            dupl.sort()
        else:
            i += 1
    for d in dupl:
        answer += d[1] - d[0]
        print(d)
    return answer