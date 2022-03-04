# Função que me lembre algo.

import time
import webbrowser

intervalos = 2
contador = 0

print('O de lembrete foi ativado.')

while contador < intervalos:
    time.sleep(5)
    webbrowser.open('https://i.pinimg.com/originals/e8/4e/db/e84edb279472c7ab49e97ec276d4ffda.gif')
    contador = contador + 1