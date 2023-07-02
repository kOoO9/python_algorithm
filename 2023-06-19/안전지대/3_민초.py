def solution(board):
    answer = 0
    k = [-1,0,1]
    length = len(board)
    
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                for ki in k:
                    if 0 <= i+ki < length:
                        for kj in k:
                            if 0 <= j+kj < length:
                                if board[i+ki][j+kj] != 1:
                                    board[i+ki][j+kj] = 2
    for i in board:
        for j in i:
            if j == 0:
                answer+=1
    return answer
