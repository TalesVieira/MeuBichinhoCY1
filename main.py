# main.py

from bichinho import BichinhoVirtual

def menu():
    nome = input("Digite o nome do seu bichinho: ")
    pet = BichinhoVirtual(nome)

    while pet.humor != "Sem vida":
        pet.status()
        print("\nEscolha uma ação:")
        print("1. Comer")
        print("2. Dormir")
        print("3. Brincar")
        print("4. Tomar banho")
        print("5. Passar tempo")
        print("6. Sair")
        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            pet.comer()
        elif escolha == "2":
            pet.dormir()
        elif escolha == "3":
            pet.brincar()
        elif escolha == "4":
            pet.tomar_banho()
        elif escolha == "5":
            pet.passar_tempo()
        elif escolha == "6":
            print("Até a próxima!")
            break
        else:
            print("Opção inválida.")

    if pet.humor == "Sem vida":
        print("\nSeu bichinho não resistiu... Fim de jogo.")
        pet.mostrar_ascii()

menu()