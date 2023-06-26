import numpy as np

def solution(board):
    answer = 0
    x = np.array(board).shape[0]
    y = np.array(board).shape[1]
    for i in range(x):
        for j in range(y):
            if board[i][j] == 0:
                if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == 1:
                    continue
                if i-1 >= 0 and board[i-1][j] == 1:
                    continue
                if i-1 >= 0 and j+1 < y and board[i-1][j+1] == 1:
                    continue
                if j-1 >= 0 and board[i][j-1] == 1:
                    continue
                if j+1 < y and board[i][j+1] == 1:
                    continue
                if i+1 < x and j-1 >= 0 and board[i+1][j-1] == 1:
                    continue
                if i+1 < x and board[i+1][j] == 1:
                    continue
                if i+1 < x and j+1 < y and board[i+1][j+1] == 1:
                    continue
                answer += 1
    return answer
