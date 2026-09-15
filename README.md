# Circuito Euleriano e Algoritmo de Hierholzer

Este projeto implementa e compara algoritmos para resolver o problema do circuito euleriano em grafos.

O objetivo principal é demonstrar, em Python, como o algoritmo de Hierholzer encontra um circuito que percorre cada aresta exatamente uma vez, quando tal circuito existe.

> Problema: dado um grafo conexo, verificar se existe um circuito euleriano e, em caso afirmativo, construir um.

---

## 1. Tema e contexto

Este repositório está vinculado ao tema de circuitos eulerianos, segundo o enunciado do seminário. A ideia central é mostrar:

- a condição de existência do circuito euleriano;
- a estrutura de dados utilizada para representar o grafo;
- a implementação do algoritmo de Hierholzer;
- a comparação com o algoritmo de Fleury;
- a geração de métricas de tempo em gráfico.

---

## 2. Problema computacional

Um circuito euleriano é um caminho fechado que usa cada aresta exatamente uma vez e retorna ao vértice inicial.

Em um grafo não direcionado, a condição necessária e suficiente para a existência de um circuito euleriano é:

- o grafo deve ser conexo;
- todos os vértices devem ter grau par.

A validação dessa condição é feita em [src/validacao/check_eulerian.py](src/validacao/check_eulerian.py).

---

## 3. Objetivo do projeto

- implementar o algoritmo de Hierholzer;
- validar a condição de existência do circuito euleriano;
- comparar o desempenho com o algoritmo de Fleury;
- salvar os resultados em arquivos JSON e gerar gráfico de tempo em matplotlib;
- organizar o projeto em módulos por responsabilidade.

---

## 4. Estrutura do repositório

```text
hierholzer_grupo/
├── grafos/
│   └── listas_adjacencias.json
├── imagens/
│   └── comparacao_tempos_algoritmos.png
├── src/
│   ├── __init__.py
│   ├── algoritmos/
│   │   ├── __init__.py
│   │   ├── fleury.py
│   │   └── hierholzer.py
│   ├── execucao/
│   │   ├── __init__.py
│   │   ├── import_map.py
│   │   └── main.py
│   ├── validacao/
│   │   ├── __init__.py
│   │   └── check_eulerian.py
│   └── visualizacao/
│       ├── __init__.py
│       └── grafico_tempos.py
├── README.md
└── .git/
```

### Descrição dos módulos

- [src/algoritmos/hierholzer.py](src/algoritmos/hierholzer.py): implementação do algoritmo principal.
- [src/algoritmos/fleury.py](src/algoritmos/fleury.py): algoritmo alternativo para comparação.
- [src/validacao/check_eulerian.py](src/validacao/check_eulerian.py): verificação da condição de Euler.
- [src/execucao/import_map.py](src/execucao/import_map.py): leitura do grafo salvo em JSON.
- [src/execucao/main.py](src/execucao/main.py): ponto de entrada da aplicação.
- [src/visualizacao/grafico_tempos.py](src/visualizacao/grafico_tempos.py): geração do gráfico de comparação de tempo.
- [grafos/listas_adjacencias.json](grafos/listas_adjacencias.json): instâncias de exemplo.

---

## 5. Requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3.9+
- matplotlib

Caso não tenha a biblioteca instalada, execute:

```bash
pip install matplotlib
```

---

## 6. Como executar

No diretório raiz do projeto, rode:

```bash
python .\src\execucao\main.py
```

Esse comando:

1. lê os grafos em JSON;
2. verifica se eles satisfazem a condição de Euler;
3. executa Hierholzer e Fleury;
4. imprime os tempos de execução;
5. salva um gráfico em [imagens/comparacao_tempos_algoritmos.png](imagens/comparacao_tempos_algoritmos.png).

---

## 7. Exemplo de saída

A execução imprime métricas do tipo:

```text
Grafo 0:
  Circuito Hierholzer: [0, 1, 2, ...]
  Hierholzer: 0.000071 s
  Fleury:    0.000254 s
----------------------------------------
Grafo 1:
  Hierholzer: 0.136518 s
  Fleury:    1.204532 s
----------------------------------------
```

Além disso, ao final, é gerado um gráfico comparando os tempos dos dois algoritmos.

---

## 8. Representação do grafo

Os grafos são armazenados em listas de adjacência, por exemplo:

```python
[
    [1, 2],
    [0, 2],
    [0, 1]
]
```

Esse formato indica que, por exemplo, o vértice 0 está conectado aos vértices 1 e 2.

---

## 9. Ideia do algoritmo de Hierholzer

O algoritmo de Hierholzer funciona assim:

1. escolhe um vértice inicial;
2. percorre arestas ainda não visitadas;
3. empilha os vértices visitados;
4. quando não há mais arestas saindo do vértice atual, retrocede e registra o caminho;
5. inverte a sequência final para obter o circuito completo.

Esse processo permite construir o circuito sem repetir arestas, preservando a propriedade de Euler.

---

## 10. Validação da condição de Euler

Antes de executar o algoritmo, o programa verifica se o grafo pode ter um circuito euleriano:

- grafo conexo;
- todos os vértices com grau par.

Se a condição falhar, o programa informa que o grafo não possui circuito euleriano.

---

## 11. Comparação com Fleury

O algoritmo de Fleury também resolve o problema, mas costuma ser mais lento em instâncias maiores. O projeto compara os dois tempos para ilustrar a diferença de desempenho.

---

## 12. Observações finais

- O projeto foi organizado por responsabilidade para ficar mais claro e mais adequado a uma avaliação acadêmica.
- O gráfico gerado em [imagens/comparacao_tempos_algoritmos.png](imagens/comparacao_tempos_algoritmos.png) ajuda na análise comparativa entre algoritmos.
- A estrutura atual facilita a manutenção do código e a apresentação do trabalho.

---

## 13. Licença

Este projeto é de uso acadêmico e foi desenvolvido para fins de estudo e apresentação do tema de circuitos eulerianos.
