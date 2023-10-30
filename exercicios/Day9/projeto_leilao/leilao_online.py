import json
import time
from exercicios.Day9.projeto_leilao.clearTerminal import clear_console
from exercicios.Day9.projeto_leilao.lances import lances, maior_valor

run = False
while not run:
    name = input('digite seu nome  ')
    lance = float(input('digite seu lance  '))

    lances(name, lance)
    print(f'Olá {name} seu lance foi R$:{lance}')

    restart = input("Quer continuar  ? \n ")
    time.sleep(1)
    clear_console()
    valores = maior_valor()
    if restart == 'nao':
        run = True
        maior_lance = max(valores)
        print(f'O maior lance foi de {name} de R$:{maior_lance}')
        with open('reg_de_lances.json', 'w') as f:
            json.dump([], f, indent=4)

