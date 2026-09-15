import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.algoritmos import hierholzer
from src.algoritmos import fleury
from src.execucao import import_map
from src.validacao.check_eulerian import isEulerCircuit
from src.visualizacao.grafico_tempos import salvar_grafico_tempos


def comparar_algoritmos():
    grafos = import_map.import_json()

    if not grafos:
        print("Nenhum grafo encontrado em listas_adjacencias.json.")
        return

    metricas = []

    for indice, grafo in enumerate(grafos):
        if not grafo:
            print(f"Grafo {indice}: vazio.")
            continue

        estado = isEulerCircuit(grafo)
        if estado == 0:
            print(f"Grafo {indice}: não possui circuito euleriano.")
            continue

        grafo_hierholzer = [lista[:] for lista in grafo]
        grafo_fleury = {vertice: lista[:] for vertice, lista in enumerate(grafo)}

        inicio = time.perf_counter()
        circuito_hierholzer = hierholzer.returnCircuit(grafo_hierholzer)
        tempo_hierholzer = time.perf_counter() - inicio

        inicio = time.perf_counter()
        circuito_fleury = fleury.circuito_euleriano(grafo_fleury, inicio=0)
        tempo_fleury = time.perf_counter() - inicio

        metricas.append({
            "grafo": f"Grafo {indice}",
            "Hierholzer": tempo_hierholzer,
            "Fleury": tempo_fleury,
        })

        print(f"Grafo {indice}:")
        print(f"  Circuito Hierholzer: {circuito_hierholzer}")
        print(f"  Hierholzer: {tempo_hierholzer:.6f} s")
        print(f"  Fleury:    {tempo_fleury:.6f} s")
        print("-" * 40)

    if metricas:
        caminho = salvar_grafico_tempos(metricas, pasta_saida="imagens")
        if caminho:
            print(f"Gráfico salvo em: {caminho}")


def main():
    comparar_algoritmos()


if __name__ == "__main__":
    main()
