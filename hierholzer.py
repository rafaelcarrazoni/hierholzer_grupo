def returnCircuit(adj: list[list[int]]) -> list[int]:
    if not adj:
        return []

    adj = [list(neighbors) for neighbors in adj]

    start = next((i for i in range(len(adj)) if adj[i]), 0)
    stack = [start]
    circuit = []

    while stack:
        current = stack[-1]
        if adj[current]:
            neighbor = adj[current].pop()
            if neighbor in adj and current in adj[neighbor]:
                try:
                    adj[neighbor].remove(current)
                except ValueError:
                    pass
            stack.append(neighbor)
        else:
            circuit.append(current)
            stack.pop()

    circuit.reverse()
    return circuit
