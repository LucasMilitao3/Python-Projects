def CalculaIMC() :
    print('Bem vindo ao IMC')

    # Recebe as características do cliente e converte as variaveis de str para int
    # Comandos sep="-" e end="\n" serão usados para organizar as linhas

    altura_in = input("Digite sua altura: ")
    peso_in = input('Digite seu peso: ')
    altura = float(altura_in)
    peso = float(peso_in)
    print('')

    # Calcula e exibe o IMC do usuário
    imc: float = peso / (altura * altura)

    # Objetos com as modalidades de IMC de uma pessoa
    magro = imc < 18.5
    normal = 18.5 <= imc < 24.9
    sobrepeso = 25 < imc <= 29.9
    obeso = 30 < imc <= 39.9
    obesidademorbida = imc > 40

    # Verificando em qual categoria de IMC o cliente se enquadra.
    if (magro):
        print('Seu IMC é:', imc, '.Voce é considerado Magro')
        print('')
    elif (normal):
        print('Seu IMC é:', imc, '.Voce é considerado Normal')
        print('')
    elif (sobrepeso):
        print('Seu IMC é:', imc, '.Voce é considerado com Sobrepeso')
        print('')
    elif (obeso):
        print('Seu IMC é:', imc, '.Voce é considerado Obeso')
        print('')
    elif (obesidademorbida) :
        print('Seu IMC é:', imc, '.Voce é considerado Obeso Mórbido')
        print('')
    else:
        pass

    # Orientações finais ao usuário
    print('---> Compare seu IMC na tabela:', imc)

    print('Abaixo a tabela de IMC')
    print('')

    # Tabela de IMC
    print('MENOR QUE  18,5 MAGREZA')
    print('ENTRE 18,5 E 24,9 NORMAL ')
    print('ENTRE 25,0 E 29,9 SOBREPESO ')
    print('ENTRE 30,0 E 39,9 OBESIDADE')
    print('MAIOR QUE 40,0 OBESIDADE MORBIDA')


if __name__ == "__main__":
    CalculaIMC()
