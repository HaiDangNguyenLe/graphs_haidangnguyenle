from collections import deque


def bfs(graph, source):
    visited = set() #
    queue = deque([source]) 
    order = []
    while queue:
        u = queue.popleft()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)

        for v in graph.get(u, {}):
            if v not in visited:
                queue.append(v)     
    return order