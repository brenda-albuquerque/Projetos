from random import randint
from time import sleep
from rich import print

tentativas = 1
pontosplayer = 0
pontosbot = 0

itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0, 2)

print("\033[1;33;44mBem-vindo(a) ao Jokenpô!:robot:\033[m")
print(' ')
nome = input("\033[1;34mQual seu nome jogador(a)? ")
print(' ')
print("Você tem 5 chances para vencer o Mr.Robot :Robot:.")
print(f'''Vamos la, {nome}!
     Suas opções são:
     [0] Pedra
     [1] Papel
     [2] Tesoura\033[m''')

while tentativas <= 5:

    jogador = int(input("\033[1;34m[0] Pedra, [1] Papel ou [2] Tesoura? \033[m"))
    print('\033[1;33;44m    J  O      \033[m')
    sleep(0.5)
    print("\033[1;33;44m      K  E  N      \033[m")
    sleep(0.5)
    print("\033[1;33;44m             P  Ô!     \033[m")
    sleep(1)
    print(' ')
    print('\033[1;33m -=- \033[m' * 6)
    print(f"\033[1;34mO Mr.robot :robot: escolheu: {itens[bot]}\033[m")
    print(f"\033[1;34mO Jogador(a), {nome} escolheu: {itens[jogador]}\033[m")
    print('\033[1;33m -=- \033[m' * 6)
    # Pedra
    if bot == 0:
        if jogador == 0:
            print("\033[1;33mEmpate\033[m")
        elif jogador == 1:
            print(f"\033[1;32mPonto para {nome}!\033[m")
            pontosplayer = pontosplayer + 1
        elif jogador == 2:
            print(f"\033[1;31mPonto para o Mr.Robot! :robot:\033[m")
            pontosbot = pontosbot + 1
        else:
            print("\033[7;31;10mJogada Inválida!\033[m")
    # Papel
    if bot == 1:
        if jogador == 0:
            print(f"\033[1;31mPonto para o Mr.Robot! :robot:\033[m")
            pontosbot = pontosbot + 1
        elif jogador == 1:
            print("\033[1;33mEmpate\033[m")
        elif jogador == 2:
            print(f"\033[1;32mPonto para {nome}!\033[m")
            pontosplayer = pontosplayer + 1
        else:
            print("\033[7;31;10mJogada Inválida!\033[m")
    # Tesoura
    if bot == 2:
        if jogador == 0:
            print(f"\033[1;32mPonto para {nome}!\033[m")
            pontosplayer = pontosplayer + 1
        elif jogador == 1:
            print(f"\033[1;31mPonto para o Mr.Robot! :robot:\033[m")
            pontosbot = pontosbot + 1
        elif jogador == 2:
            print("\033[1;33mEmpate\033[m")
        else:
            print("\033[7;31;10mJogada Inválida!\033[m")
    # Fim
    if tentativas == 8:
        break
    tentativas = tentativas + 1

if pontosplayer > pontosbot:
    print(' ')
    print(f"\033[1;32mPARABÉNS JOGADOR(a), {nome}! VOCÊ VENCEU!\033[m")
    print(f'''\033[1;36mPLACAR = Mr. Robot :Robot: = {pontosbot}
        Jogador(a), {nome} = {pontosplayer}\033[m''')
elif pontosbot > pontosplayer:
    print(' ')
    print("\033[1;31m### GAME-OVER ###")
    print('''O vencedor é o Mr.Robot :Robot:!\033[m''')
    print(f'''\033[1;36mPLACAR = Mr. Robot :Robot: = {pontosbot}
        Jogador(a), {nome} = {pontosplayer}
    Tente novamente\033[m''')
else:
    print(' ')
    print("\033[1;33mEMPATE\033[m")
    print(f'''\033[1;36mPLACAR = Mr.Robot:Robot: = {pontosbot}
        Jogador(a), {nome} = {pontosplayer}\033[m''')
