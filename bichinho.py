# bichinho.py

import random
import time
from constantes import Cor, COMIDAS_SAUDAVEIS, COMIDAS_NAO_SAUDAVEIS, GELADEIRA_PADRAO
from util import evento_aleatorio, verificar_conquistas

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.energia = 100
        self.fome = 30
        self.humor = "Feliz"
        self.acoes = 0
        self.personalidade = random.choice(["Curioso", "Preguiçoso", "Brincalhão"])

        # Para rastrear conquistas
        self.acoes_tipo = set()           # marca tipos de ação já feitas ('comer','dormir','brincar','banho','passar_tempo')
        self.conquistas_marcadas = set()  # marca milestones já exibidas (10,25,50)

    def mostrar_ascii(self):
        print(f"\n{Cor.AZUL}Humor atual: {self.humor} | Personalidade: {self.personalidade}{Cor.RESET}")

        if self.humor == "Feliz":
            print(Cor.VERDE + """
          (\\__/)
          ( ^‿^ )  ✨
         / >🍎< \\ 
        """ + Cor.RESET)

        elif self.humor == "Neutro":
            print(Cor.AMARELO + """
          (\\__/)
          ( -_- )
         /  | |  \\ 
        """ + Cor.RESET)

        elif self.humor == "Triste":
            print(Cor.CINZA + """
          (\\__/)
          ( T_T )
         /︶︶︶\\
        """ + Cor.RESET)

        elif self.humor == "Sem vida":
            print(Cor.VERMELHO + """
          (\\__/)
          ( x_x )
         /  RIP  \\ 
        """ + Cor.RESET)

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
        # Mostra 6 itens aleatórios da geladeira (ou menos se a geladeira tiver menos itens)
        k = min(6, len(GELADEIRA_PADRAO))
        opcao_lista = random.sample(GELADEIRA_PADRAO, k)

        print("\nA geladeira contém:")
        for idx, item in enumerate(opcao_lista, start=1):
            print(f"{idx}. {item.capitalize()}")

        escolha = input("Escolha o número do alimento (ou 'c' para cancelar): ").strip().lower()
        if escolha == 'c':
            print("Ação cancelada.")
            return

        if not escolha.isdigit() or not (1 <= int(escolha) <= len(opcao_lista)):
            print("Escolha inválida.")
            return

        comida = opcao_lista[int(escolha) - 1]
        print(f"\nVocê pegou: {comida}...")
        time.sleep(1)

        # Aplica efeitos conforme listas de saudáveis/não saudáveis
        if comida in COMIDAS_SAUDAVEIS:
            self.saude = min(100, self.saude + 15)
            self.fome = max(0, self.fome - 20)
            if self.personalidade == "Curioso":
                self.humor = "Feliz"
            else:
                self.humor = "Neutro"
            print(Cor.VERDE + f"{self.nome} comeu {comida} e se sentiu melhor." + Cor.RESET)

        elif comida in COMIDAS_NAO_SAUDAVEIS:
            self.saude = max(0, self.saude - 10)
            self.fome = max(0, self.fome - 20)
            self.humor = "Feliz"
            print(Cor.AMARELO + f"{self.nome} comeu {comida} (gostoso, mas não tão saudável)." + Cor.RESET)

        else:
            # Caso o item não esteja em nenhuma lista: efeito neutro leve
            self.fome = max(0, self.fome - 15)
            self.humor = "Neutro"
            print(Cor.CIANO + f"{comida} é um item estranho... efeito neutro." + Cor.RESET)

        # incremento de ações e verificação de conquistas
        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self, 'comer')
        self.atualizar_humor()

    def dormir(self):
        print("Dormindo...")
        # animação simples
        for c in "|/-\\":
            print(f"\rDormindo... {c}", end="", flush=True)
            time.sleep(0.25)
        print("\r" + " " * 20)
        ganho = 30 + (10 if self.personalidade == "Preguiçoso" else 0)
        self.energia = min(100, self.energia + ganho)
        # dormir gasta um pouco de fome e tempo, afeta humor
        self.fome = min(100, self.fome + 20)
        self.humor = "Triste"

        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self, 'dormir')
        self.atualizar_humor()

    def tomar_banho(self):
        # Tornar banho mais desafiador: custa energia, aumenta fome, pode haver risco de escorregar
        print("Tomando banho...")
        # pequeno spinner para sensação de ação
        for c in ".oO":
            print(f"\rTomando banho{c}", end="", flush=True)
            time.sleep(0.5)
        print("\r" + " " * 30)

        # Benefício base e penalidades
        beneficio_saude = 10
        custo_energia = 15
        aumento_fome = 15

        # Personalidade modifica os efeitos
        if self.personalidade == "Preguiçoso":
            # preguiçosos aproveitam mais o banho (menor custo de energia)
            custo_energia = 10
            beneficio_saude = 12
        elif self.personalidade == "Curioso":
            # curiosos gastam um pouco mais explorando (mais fome)
            aumento_fome += 5

        # Aplica efeitos
        self.saude = min(100, self.saude + beneficio_saude)
        self.energia = max(0, self.energia - custo_energia)
        self.fome = min(100, self.fome + aumento_fome)

        # Pequena chance de evento negativo: escorregar e perder saúde
        if random.random() < 0.12:  # 12% de chance
            dano = random.randint(5, 12)
            self.saude = max(0, self.saude - dano)
            print(Cor.VERMELHO + f"Oh não — {self.nome} escorregou no banho e perdeu {dano} de saúde!" + Cor.RESET)
            self.humor = "Triste"
        else:
            # banho melhora o humor, mas se estiver com pouca energia pode ficar neutro
            if self.energia < 20:
                self.humor = "Neutro"
                print(Cor.AMARELO + f"{self.nome} terminou o banho, mas está muito cansado." + Cor.RESET)
            else:
                self.humor = "Feliz"
                print(Cor.CIANO + f"{self.nome} saiu do banho revigorado!" + Cor.RESET)

        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self, 'banho')
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
        # brincar também aumenta fome levemente
        self.fome = min(100, self.fome + 8)

        self.acoes += 1
        evento_aleatorio(self)
        verificar_conquistas(self, 'brincar')
        self.atualizar_humor()

    def jogo_matematica(self):
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        resultado = eval(f"{a}{op}{b}")
        resp = input(f"Quanto é {a} {op} {b}? ")
        if resp.lstrip("-").isdigit() and int(resp) == resultado:
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
        verificar_conquistas(self, 'passar_tempo')
        self.atualizar_humor()