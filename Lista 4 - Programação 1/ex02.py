from typing import KeysView


dicionario = {}
menor = [0, 0, 9999.0]
for i in range(3):
    corredor = input(f"Informe o nome do corredor {i+1}: ")
    dicionario[corredor] = []
    for j in range(3):
        tempo = float(input(f'Informe a {j+1}ª volta deste corredor: '))
        dicionario[corredor].append(tempo)
        if tempo < menor[2]:
            menor = [corredor, i+1, tempo]
    dicionario[corredor] = sum(dicionario[corredor])/10
print(menor)
for i in sorted(dicionario, key=dicionario.get):
    print(i, dicionario[i])
