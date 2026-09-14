import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo triangular
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Layout fixo (posições bem distribuídas para um triângulo)
pos = nx.spring_layout(G, seed=42)

# Configura a figura
plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('#f1f1f1')

# Desenha as arestas com curvatura leve
nx.draw_networkx_edges(
    G, pos,
    width=2.5,
    edge_color='#4a4a4a',
    alpha=0.7,
    connectionstyle='arc3,rad=0.1'
)

# Desenha os nós com gradiente de cor e borda
nx.draw_networkx_nodes(
    G, pos,
    node_size=1400,
    node_color='#898989',
    edgecolors='#000000',
    linewidths=2.5
)

# Rótulos dos nós
nx.draw_networkx_labels(
    G, pos,
    font_size=16,
    font_weight='bold',
    font_color='white'
)

plt.title('', fontsize=16, fontweight='bold', color='#333333', pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()