def solution(N, number):
    # 가능한 최대의 사용 횟수를 8로 초기화
    answer = 9
    # 동적 계획법을 위한 DP 배열 초기화
    dp = [set() for _ in range(9)]  # 사용 횟수에 따라 set을 저장하는 배열

    # 1부터 8까지 사용되는 N의 개수에 대해 계산
    for i in range(1, 9):
        # 현재 사용되는 N의 개수로 만들 수 있는 수 계산
        cur_num = int(str(N) * i)
        dp[i].add(cur_num)

        # 이전 사용 횟수의 결과를 활용하여 계산
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        # 계산된 수가 number와 동일하다면 최솟값 갱신
        if number in dp[i]:
            answer = min(answer, i)
            break
            
    # 최솟값이 제한사항인 8보다 크다면 -1 반환
    return -1 if answer > 8 else answer