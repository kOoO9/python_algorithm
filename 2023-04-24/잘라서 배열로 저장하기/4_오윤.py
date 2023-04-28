def solution(my_str, n): 
    answer = []
    
    while len(my_str) > 0: #매개변수 my_str을 매개변수 n개씩 잘라낼 것이기 때문에 그 길이가 0보다 큰 동안만 실행한다.
        if len(my_str) > n:  #인덱스 범위가 my_str의 길이를 넘어가는 경우에 index 오류가 날 수도 있으므로 조건문으로 상황 분리.
            answer.append(my_str[:n]) # 슬라이싱을 이용하여 answer 리스트에 추가
            my_str = my_str[n:] #슬라이싱을 이용하여 answer에 추가한 부분 삭제
        else:
            answer.append(my_str)
            break

    return answer
