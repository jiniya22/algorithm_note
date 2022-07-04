def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

# 위의 그래프에서 각 노드가 방문했는지 여부를 판단하기 위해 정의
visited = [False] * 9
dfs(graph, 1, visited)

"""
출력 결과:
1 2 7 6 8 3 4 5 
"""