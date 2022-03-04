from random import randint
from rich import print

tentativas = 1
numero_bot = randint(1, 50)

print('--' * 21)
print("\033[1;30;44mBem-vindo(a) ao jogo Guess The Number! :robot:\33[m")
print('--' * 21)
print("\033[1;36mVocê tem 7 chances para desvendar que número o Mr.RoBot escolheu!\33[m")
print(' ')
nome = input("\033[1;34mOlá, jogador(a)! Qual o seu nome? ")
print(' ')
print(f'''Vamos lá, {nome}! (¯ ▽ ¯) ノ
Qual o seu palpite? Insira um número de 1 a 50.\33[m''')

while tentativas <= 7:

    palpite = int(input("Digite um número: "))

    if palpite > 50 or palpite <= 0:
        print("\033[1;33mApenas números de 1 a 50, jogador(a)!")
        print("	(u_u“)\33[m")
        print(' ')
        print(f"\033[1;34m¨ {tentativas} de 7 chances.¨\33[m")
    elif palpite < numero_bot:
        print("\033[1;34mÉ um número maior, tente novamente.")
        print(' ')
        print(f"¨ {tentativas} de 7 chances.¨\33[m")
# Vitória.
    elif palpite == numero_bot:
        print (' ')
        print("\033[1;32m ヽ(^◇^)/")
        print("PARABÉNS, JOGADOR(A)!!!")
        print(f"Você acertou,{nome}!\33[m")
        tentativas = 8
    else:
        print("\033[1;34mÉ um número menor, tente novamente.")
        print(' ')
        print(f"¨ {tentativas} de 7 chances.¨\33[m")
# Última tentativa.
    if tentativas == 6:
        print("\033[1;34mÚltima chance!!!")
        print("(＞﹏＜)\33[m")
# Game - over.
    elif tentativas == 7:
        print(' ')
        print('\033[1;31m       ಥ﹏ಥ')
        print(' ')
        print('m### GAME-OVER ###')
        print (f'O número do Mr.Robot :robot: era o {numero_bot}.\33[m')
    tentativas += 1
