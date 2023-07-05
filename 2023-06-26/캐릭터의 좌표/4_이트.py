def solution(keyinput, board):
    answer = [0,0]
    for k in keyinput:
        if k == "left" and answer[0] > -(board[0] // 2):
            answer[0] -= 1
        elif k == "right" and answer[0] < (board[0] // 2):
            answer[0] += 1
        elif k == "up" and answer[1] < (board[1] // 2):
            answer[1] += 1
        elif k == "down" and answer[1] > -(board[1] // 2):
            answer[1] -= 1
    return answer