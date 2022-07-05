"""
첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N <= 1,000), (1 <= M <= 1,000)
두번째 ~ N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다.
구멍이 뚫려있는 부분이 1, 막혀있는 부분이 1

한번에 만들 수 있는 얼음의 개수를 출력하세요.

입력 예시:
4 5
00110
00011
11111
00000

출력 예시:
3
"""

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

print(graph)


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:  # 범위를 벗어나면 종료
        return False
    if graph[x][y] == 0:    # 아직 현재 노드를 방문하지 않았다면
        graph[x][y] = 1     # 방문처리하고
        # 상하좌우 모두 재귀적으로 호출한다
        dfs(x - 1, y)   # 상
        dfs(x + 1, y)   # 하
        dfs(x, y - 1)   # 좌
        dfs(x, y + 1)   # 우
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)