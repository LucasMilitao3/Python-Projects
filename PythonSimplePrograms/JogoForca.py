# forca.py
import random

def Jogar():
    print("*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

#abrindo o arquivo com várias palavras de frutas    
    arquivo = open("frutas.txt", 'r')
    palavras = []

#preenchendo a lista palavras com todas as linhas do arquivo, tratando com strip
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

#selecionando uma palavra aleatória da lista palavras e padronizando a entrada com upper
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

#inserindo underline para cada letra na palavra secreta 
    letras_acertadas = ['_' for letra in palavra_secreta]    
    enforcou = False
    acertou = False
    erros = 0

#iniciando a lógica do jogo
    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = input('qual letra?')
        chute = chute.upper().strip()
        posicao = 0

#se a letra inserida pelo usuário estiver correta, inserir a letra na posição correta substituindo o underline
#se errar soma um erro, o maximo são 6 tentativas
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1
            print('Voce possui {} erros de 6'.format(erros))
            enforcou = erros == 6

#se não houver nenhum underline na palavra secreta o jogo termina com acerto
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)
        print("Jogando...")

    if acertou:
        print('Voce acertou!!')
    else:
        print('Voce perdeu...')
        print('A palavra era:', palavra_secreta)

if(__name__ == "__main__"):
    Jogar()