def solution(lines):
    answer = 0
    start = sorted(lines)[0][0]
    lines.sort(key=lambda x: (-x[1], x[0]))
    end = lines[0][1]
    
    for i in range(start, end):
        cnt = 0
        for l in lines:
            if i+0.5 in [j+0.5 for j in range(l[0], l[1])]:
                cnt += 1
            if cnt >= 2:
                answer += 1
                break
    return answer
