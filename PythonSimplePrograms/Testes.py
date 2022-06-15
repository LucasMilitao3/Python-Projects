from typing import Any

arquivo = open('frutas.txt', "r")
lista = [linha for linha in arquivo]

arquivo.close()

print(lista.strip())
