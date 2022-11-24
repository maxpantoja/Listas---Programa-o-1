def printmatriz(matriz):
    [print(x) for x in matriz]
matriz = [[str(input('Informe o nome do corredor: '))] + [int(input(f'Informe o tempo da volta {j+1}: ')) for j in range(10)] for i in range(6)]
printmatriz(matriz)