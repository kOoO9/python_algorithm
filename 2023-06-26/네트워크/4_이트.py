def solution(n, computers):
    answer = 0
    
    com = [set() for _ in range(n)]
    for i in range(n):
        for j, c in enumerate(computers[i]):
            if c == 1:
                com[i].add(j)
                
    for _ in range(2):
        for i in range(n):
            for j in range(i+1, n):
                if set(com[i]) & set(com[j]) == set():
                    continue
                com[i] = set(com[i]) | set(com[j])
                com[j] = set(com[i]) | set(com[j])
    
    return len(list(set(tuple(sorted(s)) for s in com)))