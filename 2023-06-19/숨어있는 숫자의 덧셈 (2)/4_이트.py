def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        try:
            now = int(my_string[i])
            if answer == []:
                answer.append([i, my_string[i]])
            elif answer[-1][0] == i-1:
                prev = answer[-1][1]
                answer.pop()
                answer.append([i, prev + my_string[i]])
            else:
                answer.append([i, my_string[i]])
        except:
            pass
    return sum(int(x[1]) for x in answer)