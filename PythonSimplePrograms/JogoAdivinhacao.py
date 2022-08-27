from typing import Any, Union
from random import randint

def JogaAdivinhacao():

    print("********************************************************************")
    print("*******************        BEM VINDO          **********************")
    print("******************************************************************** \n\n")

    numero_aleatorio = randint(1, 100)
    tentativas = 1
    pontos = 1000

    print("Selecione o nível de dificuldade do jogo.\n"
          "Digite (1) para Fácil - 15 tentativas \n"
          "Digite (2) para Médio - 10 tentativas \n"
          "Digite (3) para Difícil - 5 tentativas.", numero_aleatorio, '\n')

    dificuldade = 1
    level = int(input("Dificuldade: "))

    while level != 1 and level != 2 and level != 3:
        # Verifica se o input do usuário está dentro do escopo esperado da dificuldade do jogo
        print("Valor inválido")
        level = int(input("Dificuldade: "))

    if level == 1:  # Definimos o nível de dificuldade do jogo com a quantidade de tentativas
        dificuldade = 15
    elif level == 2:
        dificuldade = 10
    else:
        dificuldade = 5

    while tentativas <= dificuldade:
        # Enquanto a quantidade de tentativas forem menores que as chances definidas anteriormente o game continua
        numero_chute = int(input("Chute um numero de 1 a 100: "))

        if numero_chute == numero_aleatorio:
            print(f"Parabéns, voce acertou! Você fez {pontos} pontos")
            break
        elif numero_chute > numero_aleatorio:
            if tentativas == dificuldade:
                print(f"Você perdeu, o número secreto era: {numero_aleatorio}. Tente novamente.")
                break
            print("Seu chute está acima")
        else:
            if tentativas == dificuldade:
                print(f"Você perdeu, o número secreto era: {numero_aleatorio}. Tente novamente.")
                break
            print("Seu chute está abaixo")

        pontos_perdidos = abs(numero_aleatorio - numero_chute)  # Trecho onde subtraímos pontos do usuário
        pontos = pontos - pontos_perdidos
        print("Você tem {0} tentativas de {1}".format(tentativas, dificuldade))
        tentativas += 1

if __name__ == "__main__":
    JogaAdivinhacao()



