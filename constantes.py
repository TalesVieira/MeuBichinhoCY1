# constantes.py

class Cor:
    RESET = "\033[0m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    CINZA = "\033[90m"

# listas que determinam o efeito dos alimentos
COMIDAS_SAUDAVEIS = ["brócolis", "cenoura", "maçã", "salada", "iogurte"]
COMIDAS_NAO_SAUDAVEIS = ["pizza", "sorvete", "hambúrguer", "batata frita", "bolo"]

# opções fixas (ou misturadas) que aparecem na geladeira
GELADEIRA_PADRAO = [
    "maçã", "pizza", "cenoura", "sorvete", "iogurte",
    "hambúrguer", "brócolis", "batata frita", "salada", "bolo"
]