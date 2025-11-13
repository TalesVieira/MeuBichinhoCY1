# util.py

import random
from constantes import Cor

def evento_aleatorio(bichinho):
    chance = random.randint(1, 10)
    if chance == 1:
        print(Cor.CIANO + "Evento: Seu bichinho encontrou uma moeda brilhante!" + Cor.RESET)
    elif chance == 2:
        print(Cor.CIANO + "Evento: Ele tropeçou e perdeu um pouco de energia." + Cor.RESET)
        bichinho.energia = max(0, bichinho.energia - 10)
    elif chance == 3:
        print(Cor.CIANO + "Evento: Um amigo imaginário apareceu para brincar!" + Cor.RESET)
        bichinho.humor = "Feliz"

def verificar_conquistas(bichinho, acao_nome):
    """
    bichinho: instância de BichinhoVirtual
    acao_nome: string representando a ação executada, ex: 'comer', 'dormir', 'brincar', 'banho', 'passar_tempo'
    """

    # 1) Mensagem na primeira vez que executar determinada ação
    if acao_nome not in bichinho.acoes_tipo:
        bichinho.acoes_tipo.add(acao_nome)
        print(Cor.MAGENTA + f"🏅 Conquista: primeira vez que você fez '{acao_nome}'!" + Cor.RESET)

    # 2) Conquistas por total de ações (10, 25, 50)
    total = bichinho.acoes
    milestones = {
        10: "Você está cuidando muito bem de mim!",
        25: "Já somos grandes amigos!",
        50: "Você é o melhor tutor do mundo!"
    }

    if total in milestones and total not in bichinho.conquistas_marcadas:
        bichinho.conquistas_marcadas.add(total)
        print(Cor.MAGENTA + f"🏆 Conquista: {milestones[total]}" + Cor.RESET)