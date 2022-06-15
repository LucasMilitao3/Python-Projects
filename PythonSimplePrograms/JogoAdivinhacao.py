from typing import Any, Union
from random import randint

def JogaAdivinhacao():

    rodada = 100
    tentativa = 1
    numero_secreto = randint(1,100)
    chute_usuario = 1

    print('Bem vindo ao jogo de adivinhação mais Try Hard do mundo!, Adivinhe o numero de secreto do 1 ao 100!')


    while (tentativa <= 100):
        print('Esta é a tentativa {} de {}'.format(tentativa, rodada))
        chute_usuario = int(input("Adivinhe o numero secreto: "))

        #Declarando os argumentos para usar no if/else

        maior = chute_usuario > numero_secreto
        menor = chute_usuario < numero_secreto
        igual = chute_usuario == numero_secreto

        if (igual):
            print('Parabéns, você acertou na mosca')
            break
        elif(menor):
            print('Seu chute foi abaixo do numero secreto')
        else:
            print('Seu chute foi acima do numero secreto')

        tentativa = tentativa + 1

if __name__ == "__main__":
    JogaAdivinhacao()



