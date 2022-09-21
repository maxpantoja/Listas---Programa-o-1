with open('usuarios.txt', 'r', encoding='utf-8') as f:
    matriz = [[], []]
    for linha in f:
        matriz[0].append((linha.replace('\n', '').split(' '))[0])
        matriz[1].append((linha.replace('\n', '').split(' '))[1])
print(matriz)
