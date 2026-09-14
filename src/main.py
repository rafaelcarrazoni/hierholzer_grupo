import time
import hierholzer
import fleury
import import_map


def comparar_algoritmos():
    grafos = import_map.import_json()

    if not grafos:
        print("Nenhum grafo encontrado em listas_adjacencias.json.")
        return

    for indice, grafo in enumerate(grafos):
        if not grafo:
            print(f"Grafo {indice}: vazio.")
            continue

        grafo_hierholzer = [lista[:] for lista in grafo]
        grafo_fleury = {vertice: lista[:] for vertice, lista in enumerate(grafo)}

        inicio = time.perf_counter()
        circuito_hierholzer = hierholzer.returnCircuit(grafo_hierholzer)
        tempo_hierholzer = time.perf_counter() - inicio

        inicio = time.perf_counter()
        circuito_fleury = fleury.circuito_euleriano(grafo_fleury, inicio=0)
        tempo_fleury = time.perf_counter() - inicio

        print(f"Grafo {indice}:")
        print(f"  Hierholzer: {tempo_hierholzer:.6f} s")
        print(f"  Fleury:    {tempo_fleury:.6f} s")
        print("-" * 40)


def main():
    comparar_algoritmos()


if __name__ == "__main__":
    main()