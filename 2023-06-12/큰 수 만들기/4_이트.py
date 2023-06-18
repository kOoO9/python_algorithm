def solution(number, k):
    stack = []
    
    for num in number:
        # stack: 스택이 비어있지 않을 때
        # stack[-1] < num: 마지막 숫자가 현재 숫자보다 작을 떄
        # k > 0: 아직 제거할 개수가 남아 있을 때
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    while k > 0:
        stack.pop()
        k -= 1
        
    answer = ''.join(stack)
    return answer