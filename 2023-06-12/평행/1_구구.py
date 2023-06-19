def solution(dots):
    dots.sort()
    st = dots[0]
    for i in range(1, 4):
        g = (dots[i][1] - st[1]) / (dots[i][0] - st[0]) #기울기
        lst = [1,2,3]
        lst.remove(i)
        if i == 1 and g == (dots[lst[1]][1] - dots[lst[0]][1]) / (dots[lst[1]][0] - dots[lst[0]][0]):
            return 1
    return 0
