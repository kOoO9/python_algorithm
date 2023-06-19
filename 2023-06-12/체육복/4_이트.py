def solution(n, lost, reserve):
    lost_dd = [x for x in lost if x not in reserve]
    reserve_dd = [x for x in reserve if x not in lost]
    
    lost_dd.sort()
    lost_ = lost_dd.copy()

    for i in lost_dd:
        if i-1 in reserve_dd:
            lost_.remove(i)
            reserve_dd.remove(i-1)
            continue
        elif i+1 in reserve_dd:
            lost_.remove(i)
            reserve_dd.remove(i+1)
    answer = n - len(lost_)
    return answer