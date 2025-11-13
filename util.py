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

def verificar_conquistas(acoes):
    if acoes == 10:
        print(Cor.MAGENTA + "🏅 Conquista: Você está cuidando muito bem de mim!" + Cor.RESET)
    elif acoes == 25:
        print(Cor.MAGENTA + "🏅 Conquista: Já somos grandes amigos!" + Cor.RESET)
    elif acoes == 50:
        print(Cor.MAGENTA + "🏅 Conquista: Você é o melhor tutor do mundo!" + Cor.RESET)