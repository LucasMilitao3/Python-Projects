import IMC
import JogoAdivinhacao
import JogoForca

print('Bem vindo à Central de games! Escolha o que deseja fazer')
print('Selecione (1)Calcular IMC - (2)Jogar Adivinhação - (3) Jogar Jogo da Forca')
selecione = 0

while selecione != 1 and selecione != 2:
    selecione_str = input()
    selecione = int(selecione_str)

    if selecione == 1:
        IMC.CalculaIMC()
    elif selecione == 2:
        JogoAdivinhacao.JogaAdivinhacao()
    elif selecione == 3:
        JogoForca.Jogar()
    else:
        print('Voce deve selecionar 1, 2 ou 3')
        continue

