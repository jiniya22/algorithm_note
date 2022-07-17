"""
visited (리스트), need_visit(스택)
노드 수 V, 간선 수 E
while need_visit: 구문은 V + E 만큼 수행하기 때문에 시간복잡도는 O(V + E)
"""
from collections import deque


def dfs(graph, start):
    visited = []
    need_visit = deque()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(visited)


graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

dfs(graph, 'A')