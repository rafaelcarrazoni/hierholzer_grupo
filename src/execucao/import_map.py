import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
GRAPH_DATA_PATH = BASE_DIR / "grafos" / "listas_adjacencias.json"
OUTPUT_DATA_PATH = BASE_DIR / "listas_adjacencias.json"


def import_json():
    with open(GRAPH_DATA_PATH, "r", encoding="utf-8") as file:
        lista = json.load(file)
    return lista


def export_json(data):
    with open(OUTPUT_DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
