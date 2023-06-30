# 230624
# [PGS] 안전지대 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    # 검색 도움받음
    N = len(board)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 지뢰 설치
    boom = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                boom.append((i, j)) # 지뢰일 때의 인덱스 append

    # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    # 지뢰가 설치되지 않은 곳만 카운팅
    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1

    return count
    

    # 다른 사람 풀이
    # set와 enumerate 활용
    '''
    n = len(board)
    danger = set()

    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i + di, j + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])

    return n * n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
    '''
