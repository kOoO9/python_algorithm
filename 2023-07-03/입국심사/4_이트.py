def solution(n, times):
    low = 1
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n: break
            
        if cnt >= n:
            high = mid - 1
        else:
            low = mid + 1
            
    return(low)