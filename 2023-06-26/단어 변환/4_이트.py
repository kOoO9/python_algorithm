from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 그래프 생성
    graph = {}
    words.append(begin)
    for word in words:
        graph[word] = []
        for other_word in words:
            if word != other_word and is_one_char_diff(word, other_word):
                graph[word].append(other_word)

    # BFS 탐색
    queue = deque([(begin, 0)])  # 시작 단어와 현재 단계를 큐에 저장
    visited = set()  # 방문한 단어를 체크하기 위한 집합
    while queue:
        curr_word, step = queue.popleft()
        if curr_word == target:
            return step
        
        for next_word in graph[curr_word]:
            if next_word not in visited:
                queue.append((next_word, step + 1))
                visited.add(next_word)
    
    return 0


def is_one_char_diff(word1, word2):
    # word1과 word2가 한 글자만 다른지 확인하는 함수
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1
