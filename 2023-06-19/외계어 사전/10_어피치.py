# 230620
# [PGS] 외계어 사전 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    # s = sorted(''.join(spell))
    # string형을 sorted()해도 리턴형은 리스트임! => join 하는 의미가 없음

    s = sorted(spell)

    for d in dic:
        if s == sorted(d):
            return 1

    return 2
