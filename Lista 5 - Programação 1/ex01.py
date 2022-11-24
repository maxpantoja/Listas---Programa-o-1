#Funções
def construção(n):
    return [[int(input(f'Informe o elemento ({i+1}, {j+1}): ')) for j in range(n)] for i in range(n)]
def subtração(matriz1, matriz2):
    return [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1))] for i in range(len(matriz1))]
def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz[0]))] for i in range(len(matriz))]
def printmatriz(matriz):
    [print(x) for x in matriz]
#Construindo a Matriz
n = int(input('Informe a dimensão das matrizes: '))
print('\nConstruindo a Matriz 1:')
matriz1 = construção(n)
'''printmatriz(matriz1)
print('\nConstruindo a Matriz 2:')
matriz2 = construção(n)
printmatriz(matriz2)
#Subtraindo as matrizes
printmatriz(subtração(matriz1, matriz2))'''
printmatriz(transposta(matriz1))
