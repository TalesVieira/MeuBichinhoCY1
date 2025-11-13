# bichinho.py

import random
import time
from constantes import Cor, COMIDAS_SAUDAVEIS, COMIDAS_NAO_SAUDAVEIS
from util import evento_aleatorio, verificar_conquistas

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.energia = 100
        self.fome = 0
        self.humor = "Feliz"
        self.acoes = 0
        self.personalidade = random.choice(["Curioso", "Preguiçoso", "Brincalhão"])

    def mostrar_ascii(self):
        print(f"\n{Cor.AZUL}Humor atual: {self.humor} | Personalidade: {self.personalidade}{Cor.RESET}")
        if self.humor == "Feliz":
            print(Cor.VERDE + r"""  (\__/)  (｡♥‿♥｡) (___)__/""" + Cor.RESET)
        elif self.humor == "Neutro":
            print(Cor.AMARELO + r"""  (\__/)  (•_•)  (___)__/""" + Cor.RESET)
        elif self.humor == "Triste":
            print(Cor.CINZA + r"""  (\__/)  (╥﹏╥) (___)__/""" + Cor.RESET)
        elif self.humor == "Sem vida":
            print(Cor.VERMELHO + r"""  (\__/)  (×_×)  (___)__/""" + Cor.RESET)

    def atualizar_humor(self):
        if self.saude <= 0 or self.energia <= 0:
            self.humor = "Sem vida"
        elif self.saude > 70 and self.energia > 50:
            self.humor = "Feliz"
        elif self.saude > 40 and self.energia > 30:
            self.humor = "Neutro"
        else:
            self.humor = "Triste"

    def status(self):
        self.atualizar_humor()
        self.mostrar_ascii()
        print(f"{Cor.MAGENTA}Nome:{Cor.RESET} {self.nome}")
        print(f"{Cor.MAGENTA}Saúde:{Cor.RESET} {self.saude}")
        print(f"{Cor.MAGENTA}Energia:{Cor.RESET} {self.energia}")
        print(f"{Cor.MAGENTA}Fome:{Cor.RESET} {self.fome}")
        print(f"{Cor.MAGENTA}Ações realizadas:{Cor.RESET} {self.acoes}")

    def comer(self):
        print("\n1. Saudável\n2. Não saudável")
        escolha = input("Escolha a comida: ")
        if escolha == "1":
            comida = random.choice(COMIDAS_SAUDAVEIS)
            print(f"Comendo {comida}...")
            time.sleep(1)
            self.saude = min(100, self.saude + 15)
            self.fome = max(0, self.fome - 20)
            self.humor = "Neutro"
        elif escolha == "2":
            comida = random.choice(COMIDAS_NAO_SAUDAVEIS)
            print(f"Comendo {comida}...")
            time.sleep(1)
            self.saude = max(0, self.saude - 10)
            self.fome = max(0, self.fome - 20)
            self.humor = "Feliz"
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self.acoes)
        self.atualizar_humor()

    def dormir(self):
        print("Dormindo...")
        time.sleep(2)
        ganho = 30 + (10 if self.personalidade == "Preguiçoso" else 0)
        self.energia = min(100, self.energia + ganho)
        self.fome = min(100, self.fome + 20)
        self.humor = "Triste"
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self.acoes)
        self.atualizar_humor()

    def tomar_banho(self):
        print("Tomando banho...")
        time.sleep(2)
        self.saude = min(100, self.saude + 10)
        self.humor = "Feliz"
        print(Cor.CIANO + r"""  ~~~~~~ (•‿•)💧 /|   |\  |___|""" + Cor.RESET)
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self.acoes)
        self.atualizar_humor()

    def brincar(self):
        print("1. Matemática\n2. Adivinhação")
        jogo = input("Escolha o jogo: ")
        if jogo == "1":
            self.jogo_matematica()
        elif jogo == "2":
            self.jogo_adivinhacao()
        gasto = 20 + (10 if self.personalidade in ["Preguiçoso", "Brincalhão"] else 0)
        self.energia = max(0, self.energia - gasto)
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self.acoes)
        self.atualizar_humor()

    def jogo_matematica(self):
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        resultado = eval(f"{a}{op}{b}")
        resp = input(f"Quanto é {a} {op} {b}? ")
        if resp.isdigit() and int(resp) == resultado:
            print("Acertou!")
            self.humor = "Feliz" if self.personalidade == "Curioso" else "Neutro"
        else:
            print(f"Errou! Era {resultado}")
            self.humor = "Triste"

    def jogo_adivinhacao(self):
        numero = random.randint(1, 10)
        for i in range(3):
            palpite = input(f"Tentativa {i+1}/3: ")
            if palpite.isdigit() and int(palpite) == numero:
                print("Acertou!")
                self.humor = "Feliz" if self.personalidade == "Brincalhão" else "Neutro"
                return
            else:
                print("Errado.")
        print(f"Era {numero}")
        self.humor = "Triste"

    def passar_tempo(self):
        print("O tempo está passando...")
        time.sleep(1)
        self.energia = max(0, self.energia - 10)
        self.fome = min(100, self.fome + 10)
        self.saude = max(0, self.saude - 5)
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self.acoes)
        self.atualizar_humor()