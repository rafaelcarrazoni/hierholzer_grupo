def dfs(node, adj, visited):
    stack = [node]
    visited[node] = True

    while stack:
        current = stack.pop()
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)


def isEulerCircuit(adj):
    v = len(adj)
    if v == 0:
        return 2

    visited = [False] * v
    start = -1
    for i in range(v):
        if len(adj[i]) > 0:
            start = i
            break

    if start == -1:
        return 2

    dfs(start, adj, visited)

    for i in range(v):
        if len(adj[i]) > 0 and not visited[i]:
            return 0

    odd = 0
    for i in range(v):
        if len(adj[i]) % 2 != 0:
            odd += 1

    if odd == 0:
        return 2
    elif odd == 2:
        return 1
    return 0
