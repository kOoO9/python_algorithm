# 230625
# [PGS] 정수 삼각형 / 레벨3
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    for i in range(1, len(triangle)):
        len_i = len(triangle[i])
        for j in range(len_i):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len_i - 1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])
