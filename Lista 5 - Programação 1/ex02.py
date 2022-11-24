matriz = [[int(input(f'Informe o elemento ({i+1}, {j+1}): ')) for j in range(3)] for i in range(3)]
print(sum([sum([(1 if matriz[i][j] == 0 else 0) for j in range(3)]) for i in range(3)]))
