from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def salvar_grafico_tempos(dados, pasta_saida: str = "imagens"):
    """Cria um gráfico de comparação de tempo entre Hierholzer e Fleury.

    Args:
        dados: lista de dicionários com as chaves 'grafo', 'Hierholzer' e 'Fleury'.
        pasta_saida: nome da pasta onde o gráfico será salvo.
    """
    labels = [item["grafo"] for item in dados]
    hierholzer_tempo = [item["Hierholzer"] for item in dados]
    fleury_tempo = [item["Fleury"] for item in dados]

    if not labels:
        return None

    root = Path(__file__).resolve().parents[2]
    output_dir = root / pasta_saida
    output_dir.mkdir(exist_ok=True)

    pos = range(len(labels))
    largura = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    barras_h = ax.bar(
        [p - largura / 2 for p in pos],
        hierholzer_tempo,
        width=largura,
        label="Hierholzer",
        color="#f39c12",
        edgecolor="black",
        linewidth=1.0,
        alpha=0.9,
    )
    barras_f = ax.bar(
        [p + largura / 2 for p in pos],
        fleury_tempo,
        width=largura,
        label="Fleury",
        color="#2980b9",
        edgecolor="black",
        linewidth=1.0,
        alpha=0.9,
    )

    ax.set_title("Comparação de tempo de execução dos algoritmos", fontsize=12, fontweight="bold")
    ax.set_xlabel("Instância do grafo")
    ax.set_ylabel("Tempo (segundos)")
    ax.set_xticks(list(pos))
    ax.set_xticklabels(labels, rotation=0)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.legend(frameon=True)

    for container in (barras_h, barras_f):
        ax.bar_label(
            container,
            labels=[f"{valor:.4f}s" for valor in [bar.get_height() for bar in container]],
            padding=3,
            fontsize=8,
        )

    fig.tight_layout()

    caminho = output_dir / "comparacao_tempos_algoritmos.png"
    fig.savefig(caminho, dpi=220)
    plt.close(fig)

    return caminho
