from typing import Any

file = open('frutas.txt', "r")
lista = []

for line in file:
    line = line.strip()
    lista.append(line)
    print(line)
file.close()

