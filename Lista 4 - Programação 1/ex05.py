x = 'A' * 70
teste = 0
matriz = [['A', 'C', 'G', 'T'],[71, 103, 57, 101]]
soma = 0
if len(x) == 70:
    for i in range(70):
        if x[i] in matriz[0]:
            soma += matriz[1][matriz[0].index(x[i])] + 18
        else:
            teste = 1
            break
    if teste == 0:
        print(soma)
    else:
        print('A fita de DNA informada não é válida')
else:
    print('A fita informada não é válida')

