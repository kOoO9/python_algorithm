def solution(my_string):
    answer = 0
    n='0'
    for i in my_string:
        if i.isdigit():
            n+=i
        else:
            answer+=int(n)
            n='0'
    return answer+int(n)
