from random import choice
from time import sleep
from sys import exit

def playStage(): #O jogador faz sua jogada e a função converte a jogada em um número primo (2, 3, 5)
    while True:
        if jogadaPlayer == "pedra":
            return 2
        elif jogadaPlayer == "papel":
            return 3
        elif jogadaPlayer == "tesoura":
            return 5

def jokenpo(jogada1):

    jogadaBot = []
    jogadaBot.append(choice([2, 3, 5]))
    if jogadaBot[0] == 2:
        print("O computador escolheu pedra!")
    elif jogadaBot[0] == 3:
        print("O computador esolheu papel!")
    elif jogadaBot[0] == 5:
        print("O computador escolheu tesoura!")

    resultado = jogada1 * jogadaBot[0]
    sleep(0.5)
    if resultado == 6:
        print("Papel ganha de pedra.")
        if jogadaPlayer == "papel":
            print("O Jogador venceu!")
        else:
            print("O Computador venceu!")

    if resultado == 15:
        print("Tesoura ganha de papel.")
        if jogadaPlayer == "tesoura":
            print("O Jogador venceu!")
        else:
            print("O Computador venceu!")

    if resultado == 10:
        print("Pedra ganha de tesoura.")
        if jogadaPlayer == "pedra":
            print("O Jogador venceu!")
        else:
            print("O Computador venceu!")

    elif resultado == jogada1**2:
        print("Empate!")

print("PPT v0.1.1 por @clebbf \n")
while True:

    jogadaPlayer = str(input("O que você quer jogar? Pedra, papel, ou tesoura?: "))
    jogadaPlayer = jogadaPlayer.lower()

    if jogadaPlayer not in ["pedra","papel","tesoura"]:
        print("Faça uma jogada válida!")
        continue

    elif jogadaPlayer == "pedra" or "papel" or "tesoura":
        jokenpo(playStage())
        while True:
            resposta = input("Deseja jogar novamente? (s/n): ")
            if resposta == "s":
                break
            elif resposta == "n":
                exit(2)
            else:
                print("Resposta inválida.")
                continue



