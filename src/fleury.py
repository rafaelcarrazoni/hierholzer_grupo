from copy import deepcopy

def dfs_contagem(grafo, v, visitados):
    visitados.add(v)
    count = 1
    for viz in grafo[v]:
        if viz not in visitados:
            count += dfs_contagem(grafo, viz, visitados)
    return count


def aresta_valida(grafo, u, v):
    if len(grafo[u]) == 1:
        return True

    visitados_antes = set()
    count_antes = dfs_contagem(grafo, u, visitados_antes)

    grafo[u].remove(v)
    grafo[v].remove(u)

    visitados_depois = set()
    count_depois = dfs_contagem(grafo, u, visitados_depois)

    grafo[u].append(v)
    grafo[v].append(u)

    return count_antes == count_depois


def proxima_aresta(grafo, u):
    for v in grafo[u]:
        if aresta_valida(grafo, u, v):
            return v
    return None


def circuito_euleriano(adjacencia, inicio=None):

    grafo = deepcopy(adjacencia)  
    num_arestas = sum(len(v) for v in grafo.values()) // 2

    if inicio is None:
        inicio = next(iter(grafo))

    circuito = [inicio]
    atual = inicio

    while num_arestas > 0:
        proximo = proxima_aresta(grafo, atual)
        if proximo is None:
            raise ValueError("Grafo inválido: não foi possível completar o circuito.")

        grafo[atual].remove(proximo)
        grafo[proximo].remove(atual)
        num_arestas -= 1

        circuito.append(proximo)
        atual = proximo

    return circuito


if __name__ == "__main__":
    adjacencia = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3, 4],
        3: [2, 4],
        4: [2, 3]
    }

    circuito = circuito_euleriano(adjacencia, inicio=0)
    print("Circuito euleriano:", circuito)