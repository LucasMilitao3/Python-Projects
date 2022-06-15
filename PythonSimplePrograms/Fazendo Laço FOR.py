from typing import Any, Union
from random import randint

rodada = 3
tentativa = 1
numero_secreto = randint(1,100)
chute_usuario = 1

print('Bem vindo ao jogo de adivinhação mais Try Hard do mundo!, Adivinhe o numero de secreto do 1 ao 50!')


for tentativa in [1,2,3,4,5,6,7,8,9]:
    print('Esta é a tentativa {} de {}'.format(tentativa, rodada))
    chute_usuario_str = input("Adivinhe o numero secreto: ")
    chute_usuario = int(chute_usuario_str)
    #Declarando os argumentos para usar no if/else
    maior = chute_usuario > numero_secreto
    menor = chute_usuario < numero_secreto
    igual = chute_usuario == numero_secreto

    if chute_usuario < 1 or chute_usuario > 100:
        print('O chute tem que ser entre 1 e 50 abestado!!')
        continue

    if (igual):
        print('Parabéns, o viado daqui não é você kkkkkkk?')
        break
    else:
        if (menor):
            print('Seu chute foi abaixo do numero secreto')
        elif (maior):
            print('Seu chute foi acima do numero secreto')

print('O numero secreto era: ',numero_secreto)
print('fim do jogo')




