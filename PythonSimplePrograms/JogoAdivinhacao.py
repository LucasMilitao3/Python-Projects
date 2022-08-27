from typing import Any, Union
from random import randint

def JogaAdivinhacao():

    print("********************************************************************")
    print("*******************        BEM VINDO          **********************")
    print("******************************************************************** \n\n")

    numero_aleatorio = randint(1, 100)
    tentativas = 1
    pontos = 300

    print("Selecione o nível de dificuldade do jogo.\n"
          "Digite (1) para Fácil - 15 tentativas \n"
          "Digite (2) para Médio - 10 tentativas \n"
          "Digite (3) para Difícil - 5 tentativas.\n")

    dificuldade = 1
    level = int(input("Dificuldade: "))

    while level != 1 and level != 2 and level != 3:
        # Verifica se o input do usuário está no escopo esperado da dificuldade do jogo
        print("Valor inválido")
        level = int(input("Dificuldade: "))

    if level == 1:  # Definimos o nível de dificuldade do jogo com a quantidade de tentativas
        dificuldade = 15
        pontos -= 50
    elif level == 2:
        dificuldade = 10
        pontos -= 25
    else:
        dificuldade = 5

    for tentativas in range(tentativas, dificuldade + 1):
        # Enquanto a quantidade de tentativas forem menores que as
        # chances definidas para dificuldade anteriormente o game continua
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

if __name__ == "__main__":
    JogaAdivinhacao()

