# 230621
# [PGS] 삼각형의 완성조건 (2) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

# sides의 원소가 아닌 n
#   i) n이 가장 길지 않은 경우, max(sides) < min(sides) + n
#   ii) n이 가장 긴 경우, n < sum(sides)
# => max(sides) - min(sides) < n < sum(sides)

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1
