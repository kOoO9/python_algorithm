# 230622
# [PGS] 숨어있는 숫자의 덧셈(2) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

import re

def solution(my_string):
    my_string = re.split('[a-zA-Z]', my_string)
    my_string = list(filter(lambda x: x != '', my_string))

    return sum(map(int, my_string))
